from itertools import permutations
from collections import Counter
from .generator import Generator
from .matrix import Matrix


class Solver:
    def __init__(self):
        self.matrix_helper = Matrix()
        self.rules_combinations = {
            1: self.combinations_by_rule([1, 2, 3, 4], 1),
            2: self.combinations_by_rule([1, 2, 3, 4], 2),
            3: self.combinations_by_rule([1, 2, 3, 4], 3)
        }

    def find_common_indices(self, list1, list2):
        """Finds indices where elements in two lists are the same.

        Args:
            list1: The first list.
            list2: The second list.

        Returns:
            A list of indices where the elements in both lists are the same.
        """

        common_indices = []
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                common_indices.append(i)
        return common_indices

    def fulfill(self, matrix):
        seq = self.matrix_helper.read_matrix(matrix, "TOP_DOWN", 1, 5)

        for col in seq:
            for row in seq:
                if not isinstance(matrix[col][row], list):
                    matrix[col][row] = [1, 2, 3, 4]

        return matrix

    def check(self, list1, list2):
        return list(set(list1) & set(list2))

    def get_clue_by_rule(self, rule):
        if rule not in self.rules_combinations:
            return rule
        return self.rules_combinations[rule]

    def remove_in_sequence(self, data):
        # Identify numbers or single-item lists as priorities
        singles = {item[0] if isinstance(item, list) and len(item) == 1 else item
                   for item in data if not isinstance(item, list) or len(item) == 1}

        result = []
        for item in data:
            if isinstance(item, list):
                if len(item) == 1:
                    result.append(item)
                else:
                    # Remove numbers in the `singles` set from multi-item lists
                    updated_sequence = [x for x in item if x not in singles]
                    result.append(updated_sequence)
            else:
                result.append(item)

        sequence_counts = Counter(tuple(seq) for seq in result)
        dups_object = {seq: count for seq, count in sequence_counts.items() if count > 1}

        # TODO: remove duplications better way
        for dups in list(dups_object):
            if len(result) - len(dups) - dups_object[dups] == 0:
                for item, index in enumerate(result):
                    if result[item] != list(dups):
                        for value in dups:
                            if value in result[item]:
                                result[item].remove(value)

        return result

    def combinations_by_rule(self, buildings, rule):
        def visible_buildings(combo):
            """
            Calculate the number of visible buildings in a sequence.
            :param combo: Tuple of building heights.
            :return: Count of visible buildings.
            """
            max_height = 0
            visible_count = 0
            for height in combo:
                if height > max_height:
                    visible_count += 1
                    max_height = height
            return visible_count

        # Generate all possible psermutations of 4 buildings
        all_combinations = permutations(buildings, 4)

        # Filter combinations where exactly 3 buildings are visible
        valid_combinations = [
            combo for combo in all_combinations if visible_buildings(combo) == rule
        ]

        return valid_combinations

    def compare_lists(self, lists):
        """
        Compares multiple lists element by element.
        If the values at the same index are the same across all lists, returns that value.
        If the values are different, returns a list with all the differing unique values at that index.
        
        :param lists: A list of lists (or tuples) to compare.
        :return: A list with the comparison result.
        """
        result = []
        for index in range(len(lists[0])):
            comparison = []

            for lst in lists:
                comparison.append(lst[index])

            # Remove duplicates by converting to a set, then back to a list
            unique_comparison = list(set(comparison))

            result.append(unique_comparison)

        return result

    def solve_by_rules(self, result, size):
        for col in self.matrix_helper.read_matrix(result, 'LEFT_RIGHT'):
            if result[0][col] and result[0][col] > 0:
                all_clues = self.get_clue_by_rule(result[0][col])
                clue = self.compare_lists(all_clues)
                i = 0
                for row in self.matrix_helper.read_matrix(result, 'TOP_DOWN', 1, 5):
                    result[row][col] = clue[i]
                    i += 1

        for col in self.matrix_helper.read_matrix(result, 'TOP_DOWN', 1, 5):
            if result[size + 1][col] != 'X' and result[col][size + 1] > 0:
                all_clues = self.get_clue_by_rule(result[col][size + 1])
                clue = self.compare_lists(all_clues)
                i = 0
                for row in self.matrix_helper.read_matrix(result, 'RIGHT_LEFT', 1, 4):
                    if isinstance(result[col][row], list):
                        result[col][row] = self.check(clue[i], result[col][row])
                    else:
                        result[col][row] = clue[i]
                    i += 1

        for col in self.matrix_helper.read_matrix(result, 'RIGHT_LEFT', 1, 4):
            if result[size + 1][col] != 'X' and result[size + 1][col] > 0:
                all_clues = self.get_clue_by_rule(result[size + 1][col])
                clue = self.compare_lists(all_clues)
                i = 0
                for row in self.matrix_helper.read_matrix(result, 'DOWN_TOP', 1, 4):
                    if isinstance(result[col][row], list):
                        result[col][row] = self.check(clue[i], result[col][row])
                    else:
                        result[col][row] = clue[i]
                    i += 1

        for col in self.matrix_helper.read_matrix(result, 'DOWN_TOP', 1, 4):
            if result[col][0] != 'X' and result[col][0] > 0:
                all_clues = self.get_clue_by_rule(result[col][0])
                clue = self.compare_lists(all_clues)
                i = 0
                for row in self.matrix_helper.read_matrix(result, 'LEFT_RIGHT', 1, 4):
                    if isinstance(result[col][row], list):
                        result[col][row] = self.check(clue[i], result[col][row])
                    else:
                        result[col][row] = clue[i]
                    i += 1

        return result

    def walk_around_rules(self, matrix, size, rule_value):
        result = []
        # left to right
        rule = []
        index = -1
        for row in range(1, size + 1):
            if matrix[0][row] == rule_value:
                for col in self.matrix_helper.read_matrix(matrix, 'TOP_DOWN', 1, size + 1):
                    rule.append(matrix[col][row])
                    index = row
        if len(rule) > 0:
            result.append((rule, index, 'TOP_DOWN'))

        # top to bottom
        rule = []
        index = -1
        for col in range(1, size + 1):
            if matrix[col][size + 1] == rule_value:
                for row in self.matrix_helper.read_matrix(matrix, 'RIGHT_LEFT', 1, size):
                    rule.append(matrix[col][row])
                    index = col
        if len(rule) > 0:
            result.append((rule, index, 'RIGHT_LEFT'))

        # right to left
        rule = []
        index = -1
        for row in range(size, 0, -1):
            if matrix[size + 1][row] == rule_value:
                for col in self.matrix_helper.read_matrix(matrix, 'DOWN_TOP', 1, size):
                    rule.append(matrix[col][row])
                    index = row
        if len(rule) > 0:
            result.append((rule, index, 'DOWN_TOP'))

        # bottom to top
        rule = []
        index = -1
        for row in range(size, 0, -1):
            if matrix[row][0] == rule_value:
                for col in self.matrix_helper.read_matrix(matrix, 'LEFT_RIGHT', 1, size + 1):
                    rule.append(matrix[row][col])
                    index = row
        if len(rule) > 0:
            result.append((rule, index, 'LEFT_RIGHT'))

        return result

    def solve_by_rule_line(self, line, rule_value, size):
        result = []
        for clue in self.get_clue_by_rule(rule_value):
            is_valid = True
            for item in range(size):
                if list(clue)[item] not in line[item]:
                    is_valid = False
            if is_valid:
                result.append(clue)

        if len(result) == 1:
            return -1, result[0]

        if len(result) == 2:
            index, value = self.find_common_indices(*result)
            return index, value
        return (-1, -1)
        

    def solve_by_rules_items(self, matrix, size, rule_value):
        for value in self.walk_around_rules(matrix, size, rule_value):
            rule, search_index, direction = value
            line_index, value = self.solve_by_rule_line(rule, rule_value, size)

            # found solution
            if value != -1 and line_index == -1:
                i = 0
                for row in self.matrix_helper.read_matrix(matrix, direction, 1, size):
                    # write horizontally
                    if direction in ["TOP_DOWN", "DOWN_TOP"]:
                        j = 0
                        for row in self.matrix_helper.read_matrix(matrix, direction, 1, size + 1):
                            matrix[row][search_index] = rule[j]
                            j += 1
                    else:
                        matrix[search_index][row] = [value[i]]
                    i += 1

            if line_index > -1:
                rule[line_index] = [value]
                # write single value from line
                i = 0
                for row in self.matrix_helper.read_matrix(matrix, direction, 1, size + 1):
                    matrix[row][search_index] = rule[i]
                    i += 1

        return matrix

    def solve_by_orientation(self, seq, result, orientation):
        """
        Solving the sequence for the given orientation.
        :param seq: Sequence of indices.
        :param result: The result matrix to modify.
        :param orientation: Either "row" or "col" to specify the processing direction.
        """
        for index in seq:
            r = []
            if orientation == 'vertically':
                r = [result[row][index] for row in seq]
            elif orientation == 'horizontally':
                r = [result[index][col] for col in seq]

            ro = self.remove_in_sequence(r)

            for i, value in enumerate(ro):
                if orientation == 'vertically':
                    result[seq[i]][index] = value
                elif orientation == 'horizontally':
                    result[index][seq[i]] = value

        return result

    def normalize(self, matrix):
        for col in range(len(matrix)):
            for row in range(len(matrix[0])):
                if isinstance(matrix[col][row], list):
                    matrix[col][row] = matrix[col][row][0] if len(matrix[col][row]) == 1 else '0'
                if matrix[col][row] in [0, None]:
                    matrix[col][row] = ''

        return matrix

    def solve_puzzle(self, clues, size=4):
        generator = Generator(size)
        matrix = generator.generate_matrix(size + 2, size + 2)
        result = self.matrix_helper.apply_rule_to_matrix(matrix, clues, size)

        # start solving
        result = self.solve_by_rules(result, size)

        # fulfilling
        result = self.fulfill(result)

        has_changes = True
        index = 0
        stored_total_values = 0

        seq = self.matrix_helper.read_matrix(matrix, 'LEFT_RIGHT', 1, 5)

        checked_rules = set()
        rules_values = list(reversed(sorted(set(clues))))
        while has_changes:
            # solving
            result = self.solve_by_orientation(seq, result, 'vertically')
            result = self.solve_by_orientation(seq, result, 'horizontally')
            total_values = self.matrix_helper.is_changed(result, seq)
            if total_values == (size * size):
                has_changes = False

            # apply rules
            if stored_total_values == total_values:
                rule_value = max([v for v in rules_values if v not in checked_rules], default=None)
                if not rule_value or rule_value == 0 or index > 10:
                    has_changes = False
                else:
                    result = self.solve_by_rules_items(result, size, rule_value)
                    checked_rules.add(rule_value)
            else:
                stored_total_values = total_values

            index += 1

        result = self.normalize(result)
        self.matrix_helper.display_matrix(result)
        return result
