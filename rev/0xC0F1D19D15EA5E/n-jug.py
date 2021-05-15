#! /usr/bin/env python3
# Solution code to the n-Jug problem featured in this reverse engineering challenge:
# https://en.wikipedia.org/wiki/Water_pouring_puzzle

from typing import Dict, Set, Tuple
from queue import Queue

# CAPACITIES = (55, 23, 19, 13)
# START = (55, 0, 0, 0)

# CAPACITIES = (55, 23, 19, 13)
# START = (55, 0, 0, 0)

# CAPACITIES = (4054, 2017, 2037)
# START = (4054, 0, 0)

# CAPACITIES = (156, 83, 73)
# START = (156, 0, 0)

CAPACITIES = (92, 73, 19)
START = (92, 0, 0)

# CAPACITIES = (42, 23, 19)
# START = (42, 0, 0)

# CAPACITIES = (8, 5, 3)
# START = (8, 0, 0)

# CAPACITIES = (8, 5, 3)
# START = (8, 0, 0)

# CAPACITIES = (8, 8, 3)
# START = (8, 0, 0)
# CAPACITIES = (4, 4, 3)
# START = (4, 0, 0)

# END = (4, 4, 0)

# T = Tuple[int, int, int]
T = Tuple[int, ...]

def get_valid_pours(capacities: T, jugs: T):
    n = len(capacities)
    for i in range(n):
        for j in range(n):
            if i != j:
                emptyness_i = capacities[i] - jugs[i]
                fullness_j = jugs[j]
                pour = min(emptyness_i, fullness_j)
                jugs_buf = list(jugs)
                jugs_buf[j] -= pour
                jugs_buf[i] += pour
                result = tuple(jugs_buf)
                if result != jugs:
                    yield result

# def search(capacities: T, start: T, end: T):
#     assert len(start) == len(end) == len(capacities)
#     assert sum(start) == sum(end)
def search(capacities: T, start: T):
    assert len(start) == len(capacities)
    assert sum(start)
    n = len(capacities)
    # BFS to find shortest path(s)
    distance: Dict[T, int] = dict()
    visit_count: Dict[T, int] = dict() # increment visit_count only if not reaped
    reaped: Set[T] = set()
    frontier: 'Queue[T]' = Queue()
    # frontier_set: Set[T] = set()
    reaped.add(start)
    frontier.put_nowait(start)
    # frontier_set.add(start)
    distance[start] = 0
    visit_count[start] = 1
    # add to visited list before frontier list
    while not frontier.empty():
        front = frontier.get_nowait()
        # frontier_set.remove(front)
        # reaped.add(front)
        mycount = visit_count[front]
        mydistance = distance[front]
        for after_pour in get_valid_pours(capacities, front):
            newdistance = mydistance + 1
            if after_pour not in distance:
                distance[after_pour] = newdistance
            if newdistance == distance[after_pour]:
                if after_pour not in visit_count:
                    visit_count[after_pour] = 0
                visit_count[after_pour] += mycount
            else:
                assert after_pour in visit_count
            if after_pour not in reaped:
                reaped.add(after_pour)
                frontier.put_nowait(after_pour)
    return distance, visit_count

# print(search(CAPACITIES, START))
distance, visit_count = search(CAPACITIES, START)

# print(max(distance.items(), key=lambda i: i[1]))
max_distance = max(distance.values())
print(max_distance)
for pour, distance in distance.items():
    if distance == max_distance:
        if visit_count[pour] == 1:
            print(pour)
        else:
            print('Multi: {} {} times!'.format(pour, visit_count[pour]))
