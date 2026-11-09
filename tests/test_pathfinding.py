"""Tests de find_path. Noham ajoute les siens ici.

FakeMaze évite d'attendre Maze : find_path n'utilise que neighbours().
"""

from blackout.ai.pathfinding import find_path


class FakeMaze:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines

    def neighbours(self, x: int, y: int) -> list[tuple[int, int]]:
        candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [(a, b) for a, b in candidates if self.lines[b][a] == "."]


CORRIDOR = FakeMaze(["#####", "#...#", "###.#", "#...#", "#####"])
TWO_ROUTES = FakeMaze(["#######", "#.....#", "#.###.#", "#.....#", "#######"])
BLOCKED = FakeMaze(["#####", "#.#.#", "#####"])


def assert_valid(maze: FakeMaze, path: list[tuple[int, int]]) -> None:
    for current, following in zip(path, path[1:]):
        assert following in maze.neighbours(*current)


def test_same_start_and_goal() -> None:
    assert find_path(CORRIDOR, (1, 1), (1, 1)) == [(1, 1)]


def test_path_includes_both_ends_and_follows_floor() -> None:
    path = find_path(CORRIDOR, (1, 1), (1, 3))
    assert path[0] == (1, 1)
    assert path[-1] == (1, 3)
    assert_valid(CORRIDOR, path)


def test_path_is_the_shortest() -> None:
    assert len(find_path(TWO_ROUTES, (1, 1), (5, 1))) == 5


def test_no_path_returns_an_empty_list() -> None:
    assert find_path(BLOCKED, (1, 1), (3, 1)) == []
