class Node:
    def __init__(self, letter):
        self.letter = letter
        self.neighbors = set()

    def add_neighbor(self, neighbor_node):
        """Add a neighboring node to the current node."""
        self.neighbors.add(neighbor_node)
    
    def __repr__(self):
        return f"Node({self.letter})"
