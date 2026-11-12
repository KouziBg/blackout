# Auteur : Noham
"""Recherche du bon chemin."""

import heapq

from blackout.world.maze import Maze


def find_path(
    maze: Maze, start: tuple[int, int], goal: tuple[int, int]
) -> list[tuple[int, int]]:
    """Renvoie le plus court chemin avec A*, start et goal compris.

    Renvoie [start] si start == goal, et une liste vide s'il n'y a aucun chemin.
    Le voisinage vient uniquement de maze.neighbours().
    """
    cost = {start: 0}
    came_from = {start: None}
    heap = [(0, start)]

    while heap != []:
        priority, current = heapq.heappop(heap)

        if current == goal:
            break

        x, y = current
        for neighbour in maze.neighbours(x, y):
            new_cost = cost[current] + 1
            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                came_from[neighbour] = current
                estimate = abs(goal[0] - neighbour[0]) + abs(goal[1] - neighbour[1])
                heapq.heappush(heap, (new_cost + estimate, neighbour))

    if goal not in came_from:
        return []

    path = []
    case = goal
    while case is not None:
        path.append(case)
        case = came_from[case]
    path.reverse()
    return path
    
    raise NotImplementedError
