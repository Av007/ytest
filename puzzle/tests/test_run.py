import pytest
from ..src.matrix import Matrix
from ..src.generator import Generator
from ..src.solver import Solver


def test_random_matrix():
    size = 4
    matrix = Matrix()
    solver = Solver()
    generator = Generator(size)
    matrix_value = generator.generate_matrix(size + 2, size + 2)
    rule = generator.generate_rule()

    result = solver.solve_puzzle(rule)
    matrix.display_matrix(result)
