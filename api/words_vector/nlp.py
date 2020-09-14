import string
from nltk import ngrams
from nltk.corpus import stopwords as stwords
from nltk.tokenize import word_tokenize
from .models import Logs


class NLP:
    def remove_stopwords(self, words):
        stopwords = set(stwords.words('portuguese') + list(string.punctuation))
        return [word for word in words if word not in stopwords]

    def tokenize(self, text):
        text = text.replace('-', ' ')
        return word_tokenize(text.lower())

    def n_grams(self, n, text):
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        n_grams = ngrams(text.split(), n)
        return [' '.join(grams) for grams in n_grams]

    def frequency(self, words, vocabulary):
        count = {}
        for vword in vocabulary:
            count[vword] = 0
        for word in words:
            if word in vocabulary:
                count[word] += 1
        return count


class NLPPIpeline:
    def __init__(self, files, _type='bow', log=True, with_vectors=True):
        self.files = files
        self.type = _type
        self.log = log
        self.files_dicts = []
        self.all_text = ''
        self.vocabulary = []
        self.vectors = []
        self.nlp = NLP()
        self.with_vectors = with_vectors

    def step1_load_file_to_dict(self):
        self.files_dicts = [
            dict(
                file_name=self.files[file].name,
                file_ontent=self.files[file].readlines(),
            )
            for file in self.files
        ]

    def step2_extract_text_from_files(self):
        text = ''
        for file in self.files_dicts:
            try:
                new_string = file['file_ontent'][0].decode('UTF-8').rstrip('\r\n')
            except Exception:
                new_string = file['file_ontent'][0].rstrip('\r\n')
            text = text + ' ' + new_string
        self.all_text = text.strip()

    def step3_generate_vocabulary(self):
        if self.type == 'bow':
            tokens = self.nlp.tokenize(self.all_text)
        else:
            tokens = self.nlp.n_grams(2, self.all_text)
        self.vocabulary = self.nlp.remove_stopwords(
            (sorted(set(tokens), key=tokens.index))
        )

    def step4_generate_vectors(self):
        for file in self.files_dicts:
            try:
                text = file['file_ontent'][0].decode('UTF-8').rstrip('\r\n')
            except Exception:
                text = file['file_ontent'][0].rstrip('\r\n')
            if self.type == 'bow':
                tokens = self.nlp.tokenize(text)
            else:
                tokens = self.nlp.n_grams(2, text)
            frequency = self.nlp.frequency(tokens, self.vocabulary)
            self.vectors.append(
                dict(name=file['file_name'], vector=list(frequency.values()))
            )

    def save_logs(self):
        files = [file['file_name'] for file in self.files_dicts]
        vector_list = [
            vector['name']
            + ' ['
            + ','.join([str(elem) for elem in vector['vector']])
            + ']'
            for vector in self.vectors
        ]

        Logs.objects.create(
            files=files, vocabulary=self.vocabulary, vectors=vector_list
        )

    def run(self):
        self.step1_load_file_to_dict()
        self.step2_extract_text_from_files()
        self.step3_generate_vocabulary()
        if self.with_vectors:
            self.step4_generate_vectors()
        self.save_logs()
