# Blackout

## Sujet

Blackout est un jeu d'horreur et d'infiltration en vue subjective. Le joueur est
coincé dans un sous-sol plongé dans le noir et poursuivi par un monstre. Il doit
trouver 3 fusibles pour ouvrir la sortie, puis survivre à des étages de plus en
plus difficiles.

Le labyrinthe est une grille 2D et la fausse 3D est calculée par raycasting. Le
raycaster est écrit par le groupe, sans moteur 3D.

## Installation

Il faut Python 3.10 ou plus.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -e ".[dev]"
```

## Utilisation

```bash
python -m blackout
```

| Touche | Action |
|---|---|
| Z ou flèche haut | Avancer |
| S ou flèche bas | Reculer |
| Q ou flèche gauche | Tourner à gauche |
| D ou flèche droite | Tourner à droite |
| Échap | Quitter |

Pour lancer les tests :

```bash
pytest
```

## Organisation du projet

L'architecture et les conventions sont décrites dans
[`docs/architecture.md`](docs/architecture.md).

Les ressources sont dans `src/blackout/assets/` :

- `maps/` : cartes au format texte (`#` pour un mur, `.` pour le sol)
- `textures/` : images des murs et des sprites
- `sounds/` : sons du jeu

## Membres du groupe et contributions

| Membre | Numéro étudiant | Contributions |
|---|---|---|
| ZAATOUT Chamssedine | 20252248 | Moteur de rendu, lancer de rayons |
| HAJJY Hamza | 20251554 | Boucle de jeu, joueur, interface, sprites |
| ABBA Maximilien | 20250212 | Labyrinthe, génération, étages, objets |
| COUTE Noham | 20251584| Monstre, recherche de chemin, machine à états |
