import nltk

doc1 = 'Jina is a neural search framework'
doc2 = 'Jina is built with cutting age technology called deep learning'


def tokenize_and_stem(doc1, doc2):
    tokens = nltk.word_tokenize(doc1 + doc2)
    stemmer = nltk.stem.porter.PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return sorted(stemmed_tokens)


def encode(vocab, doc):
    encoded = [0] * len(vocab)  #
    for idx, token in enumerate(vocab):
        if token in doc:
            encoded[idx] = 1  # present
    return encoded


if __name__ == '__main__':
    tokens = tokenize_and_stem(doc1, doc2)
    encoded_doc1 = encode(vocab=tokens, doc=doc1)
    print(encoded_doc1)
