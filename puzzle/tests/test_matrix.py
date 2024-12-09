import pytest
from ..src.matrix import Matrix


class TestMatrix:
    @pytest.fixture
    def matrix(self):
        return Matrix()

    def test_solve_puzzle(self, matrix):
        seq = matrix.read_matrix([[1, 2], [1, 2]], "LEFT_RIGHT", 0, 1)
        assert range(0, 1) == seq

    def test_solve_puzzle_reverse(self, matrix):
        seq = matrix.read_matrix([[1, 2], [1, 2]], "RIGHT_LEFT", 0, 1)
        assert range(1, -1, -1) == seq

    def test_read_matrix(self, matrix):
        matrix_value = [
            [None, 1, 1, 1, 1, None],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [None, 1, 1, 1, 1, None]
        ]
        result = matrix.read_matrix(matrix_value, 'TOP_DOWN')
        assert result == range(0, 6)

    def test_apply_rule_to_matrix(self, matrix):
        matrix_value = [
            [None, 1, 1, 1, 1, None],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [None, 1, 1, 1, 1, None]
        ]
        result = matrix.apply_rule_to_matrix(matrix_value, [1] * 16, 4)
        assert result == [
            [None, 1, 1, 1, 1, None],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [None, 1, 1, 1, 1, None]
        ]

    def test_is_changed(self, matrix):
        result = matrix.is_changed([[1, 2], [1, 2]], range(0, 2))
        assert result == 0

    def test_display_matrix(self, matrix):
        result = matrix.display_matrix([[1, 2], [1, 2]])
        assert result == None
