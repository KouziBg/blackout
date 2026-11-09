"""Tests de Maze. Maximilien ajoute les siens ici."""

import pytest

from blackout import config
from blackout.world.maze import Cell, Maze

SMALL = """\
#####
#...#
#.#.#
#...#
#####
"""


def reachable_floor(maze: Maze) -> set[tuple[int, int]]:
    floors = [
        (x, y)
        for y in range(maze.height)
        for x in range(maze.width)
        if maze.cells[y][x] is Cell.FLOOR
    ]
    seen = {floors[0]}
    stack = [floors[0]]
    while stack:
        for cell in maze.neighbours(*stack.pop()):
            if cell not in seen:
                seen.add(cell)
                stack.append(cell)
    assert seen <= set(floors)
    return seen if len(seen) == len(floors) else set()


def test_from_text_reads_size_and_cells() -> None:
    maze = Maze.from_text(SMALL)
    assert (maze.width, maze.height) == (5, 5)
    assert maze.cells[1][1] is Cell.FLOOR
    assert maze.cells[2][2] is Cell.WALL


def test_from_text_rejects_uneven_lines() -> None:
    with pytest.raises(ValueError):
        Maze.from_text("###\n##\n")


def test_from_file_loads_test_map() -> None:
    maze = Maze.from_file(config.TEST_MAP)
    assert (maze.width, maze.height) == (9, 9)


def test_is_wall_uses_x_then_y() -> None:
    maze = Maze.from_text("####\n#..#\n##.#\n####\n")
    assert not maze.is_wall(2, 2)
    assert maze.is_wall(1, 2)


def test_outside_the_grid_is_a_wall() -> None:
    maze = Maze.from_text(SMALL)
    assert maze.is_wall(-1, 1)
    assert maze.is_wall(1, 5)


def test_neighbours_ignore_walls_and_diagonals() -> None:
    maze = Maze.from_text(SMALL)
    assert set(maze.neighbours(1, 1)) == {(2, 1), (1, 2)}


def test_wall_positions_lists_every_wall() -> None:
    positions = Maze.from_text(SMALL).wall_positions()
    assert len(positions) == 17
    assert (2, 2) in positions
    assert (1, 1) not in positions


def test_generate_closes_the_border() -> None:
    maze = Maze.generate(21, 15, seed=1)
    assert all(maze.is_wall(x, 0) and maze.is_wall(x, 14) for x in range(21))
    assert all(maze.is_wall(0, y) and maze.is_wall(20, y) for y in range(15))


def test_generate_connects_every_floor_cell() -> None:
    assert reachable_floor(Maze.generate(21, 21, seed=2))


def test_generate_is_reproducible_with_a_seed() -> None:
    assert Maze.generate(21, 21, seed=3).cells == Maze.generate(21, 21, seed=3).cells


@pytest.mark.parametrize("size", [(4, 21), (21, 4), (3, 3)])
def test_generate_rejects_invalid_sizes(size: tuple[int, int]) -> None:
    with pytest.raises(ValueError):
        Maze.generate(*size)
