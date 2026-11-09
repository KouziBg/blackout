# Tâches jusqu'au TD du 13/11

**Objectif :** se déplacer dans la carte fixe en 3D, avec des murs unis.

| Membre | Fichiers | Terminé quand |
|---|---|---|
| Chamss | `world/rays.py`, `engine/raycaster.py` | Les murs s'affichent sans effet fish-eye |
| Hamza | `game.py`, `entities/player.py`, `ui/minimap.py` | On se déplace sans traverser les murs, avec une mini-carte |
| Maximilien | `world/maze.py`, `tests/test_maze.py` | `Maze` charge la carte, et le DFS passe les tests |
| Noham | `ai/pathfinding.py`, `tests/test_pathfinding.py`, `README.md`, `pyproject.toml` | A* passe les tests, et l'installation marche |

## Ordre de travail

Maximilien pousse `from_text`, `from_file`, `is_wall` et `neighbours` en premier,
car les autres en dépendent.

## Calendrier

- **Samedi 7/11 :** valider les conventions et les signatures.
- **Mardi 10/11 :** chacun pousse sa partie.
- **Mercredi 11/11 :** assemblage complet.
- **Jeudi 12/11 :** test du ZIP sur un autre PC, puis dépôt sur badass par Noham.

Pour créer le ZIP :

```bash
git archive -o blackout.zip HEAD
```

## Méthode Git

- Une branche par tâche, par exemple `moteur-murs`.
- On fusionne dans `main` uniquement si le jeu se lance.
- Chaque fichier indique son auteur en première ligne.
