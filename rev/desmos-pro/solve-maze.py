from typing import List, Optional, Tuple
import mazegen
from mazegen import M, WALL

# In desmos coordinates (x,y), with y=0 being the bottom row
# CARDINAL_DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# In array coordinates (y,x), with y=0 being the top row
CARDINAL_DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

S = Tuple[int, int]

class Node:
    def __init__(self, direction: int, prev: Optional['Node']):
        # dir: 0: up, 1: right, 2: down, 3: left
        self.direction = direction
        self.prev = prev

def convert_to_array_coord(height: int, desmos_coord: S) -> S:
    x = desmos_coord[0]
    y = height - 1 - desmos_coord[1]
    return y, x

# MODULO: int = 10 ** 15
MODULO: int = 1_000_000_007
PRIME = 31
OFFSET = 1

def flag_hash(list_dir: List[int]):
    h = 0
    for direction in list_dir:
        h *= PRIME
        h += direction + OFFSET
        h %= MODULO
    return h % MODULO

def modexp_table(l: int):
    return [pow(PRIME, i, MODULO) for i in range(l)]

def solve(maze: M, start: S, end: S):
    width = len(maze[0])
    height = len(maze)
    node_visited = [[False] * width for _ in range(height)]
    # prev: List[List[Optional[Node]]] = [[None] * width for _ in range(height)] # type: ignore
    none_list: List[Optional[Node]] = [None]
    node: List[List[Optional[Node]]] = [none_list * width for _ in range(height)]
    def visit(square_y: int, square_x: int):
        node_visited[square_y][square_x] = True
        for direction, (dy, dx) in enumerate(CARDINAL_DELTAS):
            ny = square_y + dy
            nx = square_x + dx
            if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] != WALL and not node_visited[ny][nx]:
                node[ny][nx] = Node(direction, node[square_y][square_x])
                visit(ny, nx)
    visit(*convert_to_array_coord(height, start))

    steps = []
    ey, ex = convert_to_array_coord(height, end)
    current_node = node[ey][ex]
    if current_node == None:
        print('No path :(')
    else:
        while current_node != None:
            steps.append(current_node.direction)
            current_node = current_node.prev
        dir_list = list(reversed(steps))
        print(dir_list)
        l = len(steps)
        print('l = {}'.format(l))
        # The modulo exponentiation table allows Desmos to compute the hash
        print('T = {}'.format(modexp_table(l)))
        print('T_mod = {}'.format(MODULO))
        print('Flag: sdctf{{{}}}'.format(flag_hash(dir_list)))

# solve(mazegen.generate_maze(21, 21, 3157464641), (0, 20), (6, 20))
# solve(mazegen.generate_maze(21, 21, 3157464641), (0, 20), (12, 20))
solve(mazegen.generate_maze(21, 21, 3157464641), (0, 20), (10, 10))
