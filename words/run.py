from src import is_word

valid_words = {'pop', 'rom', 'corn', 'popcorn', 'rock', 'mock', 'ok'}

if __name__ == '__main__':
    words = is_word(valid_words)
    assert len(words) == len(valid_words)
