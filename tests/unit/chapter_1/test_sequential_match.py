from src.chapter_1.sequential_match import match_sequentially


def test_match_sequentially():
    matches = match_sequentially()
    print(matches)
    assert isinstance(matches, list)
    assert len(matches) == 1
    assert '3.txt' in matches[0]
