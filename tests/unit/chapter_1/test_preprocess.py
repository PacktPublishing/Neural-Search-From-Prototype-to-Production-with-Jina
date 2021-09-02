from src.chapter_1.preprocess import tokenize_and_stem


def test_tokenize_and_stem():
    tokens = tokenize_and_stem()
    assert isinstance(tokens, list)
    assert len(tokens) == 14
    assert tokens == [
        'jina',
        'is',
        'a',
        'neural',
        'search',
        'framework',
        'built',
        'with',
        'cut',
        'age',
        'technolog',
        'call',
        'deep',
        'learn',
    ]
