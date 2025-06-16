import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class Mineral:
    def __init__(self, name, crystallization_temp_range, composition):
        self.name = name
        self.min_temp, self.max_temp = crystallization_temp_range
        self.composition = composition

    def crystallizes_at(self, temp):
        return self.min_temp >= temp >= self.max_temp

    def __repr__(self):
        return f"{self.name} ({self.min_temp}-{self.max_temp}°C)"


class Magma:
    def __init__(self, magma_type):
        self.magma_type = magma_type
        self.minerals = self.define_minerals()
        self.initial_composition = self.define_initial_composition()

    def define_minerals(self):
        if self.magma_type == "basaltique":
            return [
                Mineral("Olivine", (1300, 1200), {"MgO": 0.5, "FeO": 0.3, "SiO2": 0.1, "Al2O3": 0.1}),
                Mineral("Pyroxène", (1200, 1000), {"MgO": 0.3, "FeO": 0.3, "SiO2": 0.3, "Al2O3": 0.1}),
                Mineral("Amphibole", (1000, 850), {"MgO": 0.2, "FeO": 0.2, "SiO2": 0.4, "Al2O3": 0.2}),
                Mineral("Plagioclase", (1150, 850), {"MgO": 0.0, "FeO": 0.0, "SiO2": 0.5, "Al2O3": 0.5}),
                Mineral("Quartz", (800, 600), {"MgO": 0.0, "FeO": 0.0, "SiO2": 0.95, "Al2O3": 0.05})
            ]
        else:
            raise ValueError("Type de magma non pris en charge pour l'instant")

    def define_initial_composition(self):
        return {"SiO2": 50.0, "MgO": 15.0, "FeO": 15.0, "Al2O3": 20.0}

    def __repr__(self):
        return f"Magma {self.magma_type} contenant {len(self.minerals)} minéraux"


class FractionalCrystallization:
    def __init__(self, magma):
        self.magma = magma
        self.residual_composition = magma.initial_composition.copy()
        self.history = []
        self.initial_mass = 100.0  # Masse initiale arbitraire
        self.remaining_mass = self.initial_mass
        self.total_crystallized_mass = 0.0

    def run(self):
        temp = max(mineral.min_temp for mineral in self.magma.minerals)
        end_temp = min(mineral.max_temp for mineral in self.magma.minerals)

        while temp >= end_temp:
            mass_crystallized_this_step = 0.0
            for mineral in self.magma.minerals:
                if mineral.crystallizes_at(temp):
                    mass = self.crystallize_mineral(mineral)
                    mass_crystallized_this_step += mass
            self.total_crystallized_mass += mass_crystallized_this_step
            self.remaining_mass -= mass_crystallized_this_step
            self.record_state(temp)
            print(f"Température : {temp}°C - Cristallisé : {self.total_crystallized_mass:.2f} / {self.initial_mass} "
                  f"({100 * self.total_crystallized_mass / self.initial_mass:.1f}%)")
            temp -= 50

        self.plot_evolution()

    def crystallize_mineral(self, mineral):
        fraction = 0.10  # 10% du magma résiduel forme des cristaux de ce minéral
        mass_crystallized = self.remaining_mass * fraction
        for element, proportion in mineral.composition.items():
            removed_amount = self.residual_composition[element] * fraction * proportion
            self.residual_composition[element] -= removed_amount
        return mass_crystallized

    def record_state(self, temp):
        state = {"Temperature": temp}
        state.update(self.residual_composition)
        self.history.append(state)

    def plot_evolution(self):
        df = pd.DataFrame(self.history).sort_values("Temperature")
        df.set_index("Temperature", inplace=True)
        df.plot(marker='o')
        plt.gca().invert_xaxis()
        plt.title("Évolution chimique pendant la cristallisation fractionnée")
        plt.xlabel("Température (°C)")
        plt.ylabel("Teneur (%)")
        plt.grid()

        if not os.path.exists("img"):
            os.makedirs("img")

        filename = f"img/evolution_{self.magma.magma_type}.png"
        plt.savefig(filename)
        print(f"Graphique sauvegardé sous {filename}")
        plt.show()


# Exemple d'utilisation
if __name__ == "__main__":
    magma = Magma("basaltique")
    fc = FractionalCrystallization(magma)
    fc.run()
