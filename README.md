# 🌋 Simulation de Cristallisation Fractionnée d’un Magma Basaltique

Ce projet propose une **modélisation algorithmique de la cristallisation fractionnée** dans un magma basaltique, à l’aide de classes Python représentant les minéraux et le magma. L’évolution chimique est simulée et visualisée en fonction de la température décroissante.

---

## 🧪 Dépendances principales

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.26.4+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.2.3+-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8.4+-blue.svg)

![Status](https://img.shields.io/badge/Status-Prototype-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🧭 Objectif du projet

Simuler la **cristallisation fractionnée** d’un magma de type basaltique pour observer l’évolution de sa composition chimique au cours de son refroidissement. Le projet vise à illustrer les concepts géochimiques liés à la différenciation magmatique.

---

## 📂 Structure du Projet
```text
cristallisation_fractionnee/
├── simulation.py             # Script principal avec les classes et la logique de simulation
├── img/                      # Dossier contenant les graphes générés
├── requirements.txt          # Dépendances du projet
└── README.md                 # Documentation
```

---

## 🔬 Fonctionnement de la simulation

### ⚗️ Composition initiale du magma basaltique :

```python
{
  "SiO2": 50.0,
  "MgO": 15.0,
  "FeO": 15.0,
  "Al2O3": 20.0
}
```

### Minéraux simulés

| Minéral     | Intervalle de cristallisation (°C) | Composition chimique approximative |
| ----------- | ---------------------------------- | ---------------------------------- |
| Olivine     | 1300 – 1200                        | MgO, FeO, SiO2, Al2O3              |
| Pyroxène    | 1200 – 1000                        | MgO, FeO, SiO2, Al2O3              |
| Plagioclase | 1150 – 850                         | SiO2, Al2O3                        |
| Amphibole   | 1000 – 850                         | MgO, FeO, SiO2, Al2O3              |
| Quartz      | 800 – 600                          | SiO2, Al2O3                        |

### Principes de simulation :

    Le magma cristallise par paliers de 50°C.

    À chaque étape, une fraction de 10% de la masse résiduelle se cristallise sous forme de minéraux.

    La composition résiduelle du magma est ajustée à chaque étape selon les minéraux formés.

    Un graphique montre l'évolution des oxydes majeurs (SiO2, MgO, etc.) en fonction de la température.

## 📈 Résultat

Une figure est générée automatiquement dans le dossier img/ :

    Nom du fichier : evolution_basaltique.png

    Contenu : Graphe de l’évolution des concentrations en oxydes majeurs en fonction de la température.

## ▶️ Lancer la simulation
1. Cloner le projet

git clone https://github.com/votre-utilisateur/cristallisation-fractionnee.git
cd cristallisation-fractionnee

2. Installer les dépendances
pip install -r requirements.txt

3. Lancer la simulation
python simulation.py


## 🔧 Améliorations futures

    Ajouter d'autres types de magma (andésitique, rhyolitique…)

    Modifier la fraction cristallisée par palier

    Ajouter d’autres minéraux ou modifier leurs compositions

    Améliorer la visualisation (Altair, Seaborn…)

## 🔬 Architecture technique

    Langage : Python 3.10+

    Visualisation : Matplotlib

    Manipulation de données : Pandas

    Structure orientée objet : classes Mineral, Magma, FractionalCrystallization

## Contact