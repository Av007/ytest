from itertools import product
from src.node import Node


class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, letter):
        """Add a node to the graph (create a new node if it doesn't exist)."""
        if letter not in self.nodes:
            self.nodes[letter] = Node(letter)
    
    def add_edge(self, letter1, letter2):
        """Add an undirected edge between two nodes."""
        if letter1 not in self.nodes:
            self.add_node(letter1)
        if letter2 not in self.nodes:
            self.add_node(letter2)
        
        self.nodes[letter1].add_neighbor(self.nodes[letter2])
        self.nodes[letter2].add_neighbor(self.nodes[letter1])

    def is_word(self, word, valid_words):
        """Check if a word is valid."""
        return word in valid_words

    def find_words(self, valid_words):
        """Find all valid words that can be formed in the graph."""
        words_found = []

        for valid_word in valid_words:
            valid_word

        def dfs(node, current_word, visited):
            """Perform Depth-First Search (DFS) to find valid words."""
            if self.is_word(current_word, valid_words):
                words_found.append(current_word)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, current_word + neighbor.letter, visited)
                    visited.remove(neighbor)

        for start_node in self.nodes.values():
            visited = set([start_node])
            dfs(start_node, start_node.letter, visited)

        results = [word.replace('1', '') for word in words_found]
        return list(dict.fromkeys(results))

    def check_combination(self, valid_words, double_letters):
        def generate_combinations(word, letters):
            combinations = []
            for char in word:
                if char in letters:
                    combinations.append([char, char + '1'])
                else:
                    combinations.append([char])

            return [''.join(combo) for combo in product(*combinations)]
        
        all_combinations = []
        for word in valid_words:
            all_combinations.extend(generate_combinations(word, double_letters))
        
        return all_combinations
