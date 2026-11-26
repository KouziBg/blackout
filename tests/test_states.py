"""Tests de la poursuite du monstre (ChaseState et Monster.update)."""

from blackout.ai.states import ChaseState
from blackout.entities.monster import Monster
from blackout.entities.player import Player
from blackout.world.maze import Maze

# Couloir en L : on va de (1, 1) à (3, 1), puis on descend jusqu'à (3, 3).
L_CORRIDOR = Maze.from_text(
    """
    #####
    #...#
    ###.#
    ###.#
    #####
    """
)


def make_monster(x: float, y: float) -> Monster:
    return Monster(x, y, ChaseState())


def test_monster_stays_in_chase() -> None:
    monster = make_monster(1.5, 1.5)
    state = monster.state
    monster.update(Player(3.5, 3.5), L_CORRIDOR, 0.1)
    assert monster.state is state


def test_monster_moves_towards_next_cell() -> None:
    monster = make_monster(1.5, 1.5)
    monster.update(Player(3.5, 3.5), L_CORRIDOR, 0.1)
    # Vitesse 1.5 pendant 0.1 s : 0.15 case vers la droite, sans bouger en y.
    assert abs(monster.x - 1.65) < 1e-9
    assert monster.y == 1.5


def test_monster_never_goes_through_walls() -> None:
    monster = make_monster(1.5, 1.5)
    player = Player(3.5, 3.5)
    for _ in range(200):
        monster.update(player, L_CORRIDOR, 0.05)
        assert not L_CORRIDOR.is_wall(int(monster.x), int(monster.y))


def test_monster_reaches_the_player() -> None:
    monster = make_monster(1.5, 1.5)
    player = Player(3.5, 3.5)
    for _ in range(200):
        monster.update(player, L_CORRIDOR, 0.05)
    assert (monster.x, monster.y) == (3.5, 3.5)


def test_path_recomputed_only_when_player_changes_cell() -> None:
    monster = make_monster(1.5, 1.5)
    player = Player(3.5, 3.5)
    monster.update(player, L_CORRIDOR, 0.01)
    path = monster.path

    # Le joueur bouge mais reste dans la même case : même liste, pas de nouvel A*.
    player.x = 3.7
    monster.update(player, L_CORRIDOR, 0.01)
    assert monster.path is path

    # Le joueur change de case : un nouveau chemin est calculé.
    player.y = 2.5
    monster.update(player, L_CORRIDOR, 0.01)
    assert monster.path is not path
    assert monster.path[-1] == (3, 2)
