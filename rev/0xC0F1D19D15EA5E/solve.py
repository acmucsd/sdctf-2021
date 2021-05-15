#! /usr/bin/env python3
# Solution code to the n-Jug problem featured in this reverse engineering challenge:
# https://en.wikipedia.org/wiki/Water_pouring_puzzle

from typing import Dict, List, Optional, Set, Tuple
from queue import Queue

class Node:
    def __init__(self, from_: int, to: int, next: Optional['Node']):
        self.from_ = from_
        self.to = to
        self.next = next

CAPACITIES = (92, 73, 19)
START = (92, 0, 0)
END = (46, 46, 0)

# CAPACITIES = (8, 5, 3)
# START = (8, 0, 0)
# END = (4, 4, 0)

T = Tuple[int, int, int]

def get_valid_pours(capacities: T, jugs: T):
    n = len(capacities)
    for i in range(n): # to
        for j in range(n): # from
            if i != j:
                emptyness_i = capacities[i] - jugs[i]
                fullness_j = jugs[j]
                pour = min(emptyness_i, fullness_j)
                jugs_buf = list(jugs)
                jugs_buf[j] -= pour
                jugs_buf[i] += pour
                result = tuple(jugs_buf)
                if result != jugs:
                    yield j, i, result

# def search(capacities: T, start: T, end: T):
#     assert len(start) == len(end) == len(capacities)
#     assert sum(start) == sum(end)
def search(capacities: T, start: T, end: T):
    assert len(start) == len(capacities)
    assert sum(start)
    # BFS to find shortest path(s)
    distance: Dict[T, int] = dict()
    visit_count: Dict[T, int] = dict() # increment visit_count only if not reaped
    path: Dict[T, Optional[Node]] = dict()
    reaped: Set[T] = set()
    frontier: 'Queue[T]' = Queue()
    # frontier_set: Set[T] = set()
    reaped.add(start)
    frontier.put_nowait(start)
    # frontier_set.add(start)
    distance[start] = 0
    visit_count[start] = 1
    path[start] = None
    # add to visited list before frontier list
    while not frontier.empty():
        front = frontier.get_nowait()
        # frontier_set.remove(front)
        # reaped.add(front)
        mycount = visit_count[front]
        mydistance = distance[front]
        for from_, to, after_pour in get_valid_pours(capacities, front):
            newdistance = mydistance + 1
            if after_pour not in distance:
                distance[after_pour] = newdistance
            if newdistance == distance[after_pour]:
                if after_pour not in visit_count:
                    visit_count[after_pour] = 0
                    path[after_pour] = Node(from_, to, path[front])
                visit_count[after_pour] += mycount
            else:
                assert after_pour in visit_count
            if after_pour not in reaped:
                reaped.add(after_pour)
                frontier.put_nowait(after_pour)
    return path[end]

def str_repr(path: Optional[Node]):
    pieces: List[str] = []
    current = path
    while current != None:
        pieces.append(str(1 + current.from_) + str(1 + current.to))
        current = current.next
    # trace backwards
    return ''.join(reversed(pieces))

# print(search(CAPACITIES, START))
path = search(CAPACITIES, START, END)

print(str_repr(path))

# Password:
# 12233123312331231223312331233123312312233123312331233123122331233123312331231223312331233123312312233123312331233123122331233123312312233123312331233123122331233123312331231223312331