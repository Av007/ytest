import pytest
from ..src.generator import Generator


class TestGenerator:
    @pytest.fixture
    def generator(self):
        return Generator(4)

    def test_generate_sequence(self, generator):
        seq = generator.generate_sequence()
        assert seq == [0, 1, 2, 3]

    def test_generate_rule(self, generator):
        rule = generator.generate_rule()
        assert len(rule) == 16
