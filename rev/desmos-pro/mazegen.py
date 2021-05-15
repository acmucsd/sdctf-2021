#! /usr/bin/env python3
import random
from typing import List, Tuple

CARDINAL_DELTAS: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

EMPTY = False
WALL = True

M = List[List[bool]]

# MAZE_CHAR = {EMPTY: ' ', WALL: '#'}

# Double width for terminals
MAZE_CHAR = {EMPTY: '  ', WALL: '##'}

def generate_maze(height: int, width: int, seed: int) -> M:
    random.seed(seed)
    assert height > 0 and height % 2 == 1
    assert width > 0 and width % 2 == 1
    height_half = height // 2
    width_half = width // 2
    node_height = height_half + 1
    node_width = width_half + 1
    # 2D array
    node_visited = [[False] * node_width for _ in range(node_height)]
    h_edge = [[WALL] * width_half for _ in range(node_height)]
    v_edge = [[WALL] * node_width for _ in range(height_half)]
    def visit(y: int, x: int):
        node_visited[y][x] = True
        deltas_randomized = CARDINAL_DELTAS[:]
        random.shuffle(deltas_randomized)
        for dx, dy in deltas_randomized:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < node_width and 0 <= ny < node_height:
                if not node_visited[ny][nx]:
                    if dy != 0:
                        # vertical edge
                        v_edge[y + (dy - 1) // 2][x] = EMPTY
                    else:
                        # horizontal edge
                        h_edge[y][x + (dx - 1) // 2] = EMPTY
                    visit(ny, nx)
    visit(0, 0)
    maze = [[EMPTY] * width for _ in range(height)]
    # for y in range(node_height):
    #     for x in range(node_width):
    #         maze[y*2][x*2] = EMPTY
    for y in range(height_half):
        for x in range(width_half):
            maze[y*2+1][x*2+1] = WALL
    for y in range(node_height):
        for x in range(width_half):
            maze[y*2][x*2+1] = h_edge[y][x]
    for y in range(height_half):
        for x in range(node_width):
            maze[y*2+1][x*2] = v_edge[y][x]
    return maze

def print_maze(maze: M):
    width = len(maze[0])
    # Borders
    print(MAZE_CHAR[WALL] * (width + 2))
    for row in maze:
        print(MAZE_CHAR[WALL] + ''.join(map(lambda c: MAZE_CHAR[c], row)) + MAZE_CHAR[WALL])
    print(MAZE_CHAR[WALL] * (width + 2))

if __name__ == "__main__":
    # 21x21 mazes
    # seed = 53531478
    seed = 3157464641
    seed = random.randrange(0, 2**32)
    print('Seed: {}'.format(seed))

    # print_maze(generate_maze(7, 7))
    print_maze(generate_maze(21, 21, seed))
