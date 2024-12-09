from .graph import Graph

def is_word(valid_words):
    graph = Graph()

    graph.add_edge('p', 'o')
    graph.add_edge('o', 'p1')
    graph.add_edge('p', 'p1')
    graph.add_edge('n', 'o')
    graph.add_edge('n', 'r')
    graph.add_edge('r', 'o1')
    graph.add_edge('m', 'o1')
    graph.add_edge('o1', 'k')
    graph.add_edge('o1', 'c')
    graph.add_edge('c', 'k')
    graph.add_edge('c', 'p1')

    combined_words = graph.check_combination(valid_words, ['o', 'p'])

    return graph.find_words(combined_words)
