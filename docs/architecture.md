# Architecture

## Règle principale

La logique du jeu ne dépend jamais de l'affichage.

- `world/`, `entities/` et `ai/` n'importent jamais `pygame`.
- `engine/`, `ui/` et `game.py` peuvent importer `pygame`.
- `tests/test_architecture.py` vérifie cette règle.

## Conventions

- Une case mesure 1 unité.
- `x` va vers la droite et `y` vers le bas.
- La grille se lit toujours avec `cells[y][x]`.
- Le centre de la case `(x, y)` est en `(x + 0.5, y + 0.5)`.
- Les angles sont en radians. Un angle de 0 regarde vers les `x` croissants.
- Les réglages sont dans `config.py`, jamais écrits en dur dans le code.

## Modules

| Module | Rôle | Éléments principaux |
|---|---|---|
| `config.py` | Réglages du jeu | Constantes |
| `game.py` | Boucle et états du jeu | `GameState`, `Game` |
| `world/maze.py` | Grille du labyrinthe | `Cell`, `Maze` |
| `world/rays.py` | Calcul d'un rayon, sans affichage | `RayHit`, `cast_ray` |
| `world/items.py` | Objets à ramasser | `ItemKind`, `Item` |
| `world/level.py` | Contenu d'un étage | `Level` |
| `entities/player.py` | Joueur | `Player` |
| `entities/monster.py` | Monstre | `Monster` |
| `ai/pathfinding.py` | Recherche de chemin | `find_path` |
| `ai/states.py` | Comportement du monstre | `MonsterState` et ses sous-classes |
| `engine/raycaster.py` | Dessin des murs | `render_walls` |
| `engine/sprites.py` | Dessin des sprites | `Sprite`, `render_sprites` |
| `ui/minimap.py` | Mini-carte | `draw_minimap` |
| `ui/hud.py` | Batterie et fusibles | `draw_hud` |
| `ui/menus.py` | Menus et écrans de fin | `draw_menu` |

`cast_ray` est dans `world/` car le rendu et la détection du joueur par le
monstre s'en servent tous les deux.

## Stockage des données

| Donnée | Format |
|---|---|
| Labyrinthe | `Maze.cells: list[list[Cell]]` |
| Joueur | `Player` avec `x`, `y` et `angle` |
| Objets | `dict[tuple[int, int], Item]`, avec la case comme clé |
| Chemin du monstre | `list[tuple[int, int]]` |
| Résultat d'un rayon | `RayHit` |
| Profondeur des murs | `list[float]`, une valeur par colonne |
| État de la partie | `GameState` |
