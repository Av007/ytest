import pytest
from ..src.solver import Solver

class TestSolver:
    @pytest.fixture
    def solver(self):
        return Solver()
    
    def test_solve_puzzle(self, solver):
        result = solver.solve_puzzle([0,0,1,2,0,2,0,0,0,3,0,0,0,1,0,0])
        assert result == [['', '', '', 1, 2, ''], ['', 2, 1, 4, 3, ''], ['', 3, 4, 1, 2, 2], [1, 4, 2, 3, 1, ''],[ '', 1, 3, 2, 4, ''], ['', '', '', 3, '', '']]
