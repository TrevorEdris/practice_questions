NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  # 5 has no neighbors
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}

NEIGHBORS_MATRIX = {
    0: (0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    1: (0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
    2: (0, 0, 0, 0, 0, 0, 0, 1, 0, 1),
    3: (0, 0, 0, 1, 0, 0, 0, 0, 1, 0),
    4: (1, 0, 0, 1, 0, 0, 0, 0, 0, 1),
    5: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    6: (1, 1, 0, 0, 0, 0, 0, 1, 0, 0),
    7: (0, 0, 1, 0, 0, 0, 1, 0, 0, 0),
    8: (0, 1, 0, 1, 0, 0, 0, 0, 0 ,0),
    9: (0, 0, 1, 0, 1, 0, 0, 0, 0, 0),
}

def neighbors(position):
    return NEIGHBORS_MAP[position]
