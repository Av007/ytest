from .generator import Generator


class Matrix:
    def read_matrix(self, matrix, direction, start_with_index=0, end_index=None):
        """Reads values in the matrix based on the specified direction and processes them using output_func."""
        rows = len(matrix)
        cols = len(matrix[0])

        if end_index is None:
            end_index = rows if direction in ["TOP_DOWN", "DOWN_TOP"] else cols

        # Define reading directions with dynamic ranges
        type_matrix_read = {
            "LEFT_RIGHT": range(start_with_index, end_index, 1),
            "TOP_DOWN": range(start_with_index, end_index, 1),
            "RIGHT_LEFT": range(end_index, start_with_index - 1, -1),
            "DOWN_TOP": range(rows - 1 - start_with_index, start_with_index - 1, -1)
        }

        if direction not in type_matrix_read:
            raise ValueError(f"Invalid direction '{direction}'. Valid options are: {list(type_matrix_read.keys())}")

        return type_matrix_read[direction]

    def apply_rule_to_matrix(self, matrix, rule, size):
        # generator = Generator(size)
        cols, rows = size + 2, size + 2  # adding rule fields
        # result = generator.generate_matrix(rows, cols)

        i = 0
        corners = [
            (0, 0),
            (0, rows - 1),
            (cols - 1, 0),
            (cols - 1, cols - 1),
        ]

        # Fill the top row
        for col in range(cols):
            if (0, col) in corners:
                matrix[0][col] = None
            else:
                matrix[0][col] = rule[i]
                i += 1

        # Fill the right column (excluding the already filled top and bottom corners)
        for row in range(1, rows):
            if (cols - 1, row) in corners:
                matrix[cols - 1][row] = None
            else:
                matrix[row][cols - 1] = rule[i]
                i += 1

        # Fill the bottom row (right to left)
        for col in range(cols - 2, -1, -1):
            if (col, row) in corners:
                matrix[rows - 1][col] = None
            else:
                matrix[rows - 1][col] = rule[i]
                i += 1

        # Fill the left column (bottom to top)
        for row in range(rows - 2, 0, -1):
            if (col, row) in corners:
                matrix[row][0] = None
            else:
                matrix[row][0] = rule[i]
                i += 1

        return matrix

    def is_changed(self, matrix, seq):
        total = 0
        for col in seq:
            for row in seq:
                total += len(matrix[row][col]) if isinstance(matrix[row][col], list) else 0
        return total

    def display_matrix(self, matrix):
        """
        Displays a matrix with elements wrapped in a bordered grid.

        Args:
            matrix (list of lists): A 2D array to display.

        Example:
            Input:
                [[1, 22, 3],
                [44, 5, 666]]
            Output:
                +----+----+-----+
                |  1 | 22 |   3 |
                +----+----+-----+
                | 44 |  5 | 666 |
                +----+----+-----+
        """
        # Find the width of the longest element in the matrix
        column_widths = [
            max(len(str(matrix[i][j])) for i in range(len(matrix))) for j in range(len(matrix[0]))
        ]

        # Create horizontal border
        border = "+".join("-" * (width + 2) for width in column_widths)
        border = f"+{border}+"

        # Format each row
        def format_row(row):
            return "|" + "|".join(f" {str(row[j]).rjust(column_widths[j])} " for j in range(len(row))) + "|"

        # Construct the full table
        result = [border]
        for row in matrix:
            result.append(format_row(row))
            result.append(border)

        # Print the matrix
        print("\n".join(result))
