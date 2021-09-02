import nltk

sentence = 'Jina is a neural search framework built with cutting age technology called deep learning'


def tokenize_and_stem():
    tokens = nltk.word_tokenize(sentence)
    stemmer = nltk.stem.porter.PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens


if __name__ == '__main__':
    tokens = tokenize_and_stem()
    print(tokens)
