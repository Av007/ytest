from src.solver import Solver

def solve_puzzle(clue):
    solver = Solver()
    return solver.solve_puzzle(clue)

matrix = [
    [None, 0, 0, 1, 2, None],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [None, 0, 0, 3, 0, None]
]

# matrix = [
#     [None, 0, 0, 1, 2, None],
#     [0, 2, 1, 4, 3, 0]
#     [0, 3, 4, 1, 2, 2],
#     [1, 4, 2, 3, 1, 0],
#     [0, 1, 3, 2, 4, 0],
#     [None, 0, 0, 3, 0, None]
# ]

# matrix = [
#     [None, 0, 0, 0, 0, None],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [None, 0, 0, 0, 0, None]
# ]

solve_puzzle([0, 0, 1, 2, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0])
