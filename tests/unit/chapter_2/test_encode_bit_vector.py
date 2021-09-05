from src.chapter_2.encode_bit_vector import doc1, doc2, tokenize_and_stem, encode


def test_encode():
    vocab = tokenize_and_stem(doc1, doc2)
    encoded_doc1 = encode(vocab, doc1)
    assert isinstance(encoded_doc1, list)
    assert len(encoded_doc1) == len(vocab)
    assert encoded_doc1 == [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
