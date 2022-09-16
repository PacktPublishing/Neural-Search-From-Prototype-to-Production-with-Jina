from collections import defaultdict

import numpy as np
import spacy

n_hyperplanes = 10
nlp = spacy.load('en_core_web_md')
# process 2 sentences using the model
docs = [
    nlp('What a nice day today!'),
    nlp('Hi how are you'),
]
# Get the mean vector for the entire sentence
assert docs[0].vector.shape == (300,)
# Random initialize 10 hyperplanes, dimension identical to embedding shape
hyperplanes = np.random.uniform(-10, 10, (n_hyperplanes, docs[0].vector.shape[0]))


def encode(doc, hyperplanes):
    code = np.dot(doc.vector, hyperplanes.T)  # dot product vector with norm vector
    binary_code = np.where(code > 0, 1, 0)
    return binary_code


def create_buckets(docs, hyperplanes):
    buckets = defaultdict()
    for doc in docs:
        binary_code = encode(doc, hyperplanes)
        binary_code = ''.join(map(str, binary_code))
        buckets[binary_code] = doc.text
    return buckets


if __name__ == '__main__':
    buckets = create_buckets(docs, hyperplanes)
    print(buckets)
