import random


class Generator:
    def __init__(self, size):
        self.size = size

    def generate_sequence(self):
        return list(range(0, self.size))

    def generate_matrix(self, rows, cols):
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        return matrix

    def generate_rule(self):
        rule = [0] * (self.size * self.size)

        selected_positions = random.sample(range(len(rule)), random.choice([5, 6]))
        for pos in selected_positions:
            rule[pos] = random.randint(1, self.size - 1)

        return rule
