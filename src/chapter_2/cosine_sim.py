import math

from encode_bit_vector import doc1, doc2, tokenize_and_stem, encode


def compute_cosine_sim(encoded_doc1, encoded_doc2):
    numerator = sum([i * j for i, j in zip(encoded_doc1, encoded_doc2)])
    denominator_1 = math.sqrt(sum([i * i for i in encoded_doc1]))
    denominator_2 = math.sqrt(sum([i * i for i in encoded_doc2]))
    return numerator / (denominator_1 * denominator_2)


if __name__ == '__main__':
    tokens = tokenize_and_stem(doc1, doc2)
    encoded_doc1 = encode(vocab=tokens, doc=doc1)
    encoded_doc2 = encode(vocab=tokens, doc=doc2)
    print(compute_cosine_sim(encoded_doc1, encoded_doc2))
