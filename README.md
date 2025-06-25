# 🌋 Simulation de Cristallisation Fractionnée d’un Magma Basaltique

![python](https://img.shields.io/badge/python-3.11-blue.svg)
![numpy](https://img.shields.io/badge/numpy-2.3.0-blue.svg)
![pandas](https://img.shields.io/badge/pandas-2.3.0-blue.svg)
![matplotlib](https://img.shields.io/badge/matplotlib-3.10.3-blue.svg)

---

![banner](img/banner2.jpg)

---

## Sommaire
- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Structure du projet](#-structure-du-projet)
- [Fonctionnement de la simulation](#-fonctionnement-de-la-simulation)
- [Résultat](#-résultat)
- [Installation et exécution](#️-installation-et-exécution)
- [Améliorations futures](#-améliorations-futures)
- [Architecture technique](#-architecture-technique)
- [Contact](#contact)

---

## Description

Ce projet propose une **modélisation algorithmique de la cristallisation fractionnée** dans un magma basaltique, à l’aide de classes Python représentant les minéraux et le magma. L’évolution chimique est simulée et visualisée en fonction de la température décroissante.

---
## Fonctionnalités

- Définition de minéraux avec plages de températures de cristallisation et compositions chimiques.
- Modélisation de la cristallisation progressive selon la température décroissante.
- Calcul des masses cristallisées à chaque étape.
- Visualisation graphique de la composition chimique résiduelle en fonction de la température.
- Sauvegarde automatique du graphique dans un dossier `img`.

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

## 📬Contact

Pour toute question ou suggestion :

Email : delvoyeadf@gmail.com
GitHub : @A-Delvoye