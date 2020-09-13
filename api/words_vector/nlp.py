from string import punctuation

from nltk import ngrams
from nltk.corpus import stopwords as stwords
from nltk.tokenize import word_tokenize


class NLP:
    def remove_stopwords(self, words):
        stopwords = set(stwords.words('portuguese') + list(punctuation))
        return [word for word in words if word not in stopwords]

    def tokenize(self, text):
        return word_tokenize(text.lower())

    def n_grams(self, n, text):
        return ngrams(text.split(), n)
