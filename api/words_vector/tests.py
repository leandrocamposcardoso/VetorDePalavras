from django.test import TestCase
from words_vector.nlp import NLPPIpeline


class PipelineTestCase(TestCase):
    def setUp(self):
        self.files = None
        self.files_dicts = [
            {
                'file_name': 'teste.txt',
                'file_ontent': ['Falar é fácil. Mostre-me o código.'],
            },
            {
                'file_name': 'teste2.txt',
                'file_ontent': [
                    'É fácil escrever código. Difícil é escrever código que funcione.'
                ],
            },
        ]

    def test_should_return_texts_from_all_files(self):
        self.nlp_pipeline = NLPPIpeline(
            self.files, _type='bow', log=True, with_vectors=False
        )
        self.nlp_pipeline.files_dicts = self.files_dicts
        self.nlp_pipeline.step2_extract_text_from_files()
        msg = 'Falar é fácil. Mostre-me o código. É fácil escrever código. Difícil é escrever código que funcione.'
        self.assertEqual(msg, self.nlp_pipeline.all_text)

    def test_should_return_vocabulary_with_stopwords(self):
        self.nlp_pipeline = NLPPIpeline(
            self.files, _type='bow', log=True, with_vectors=False
        )
        self.nlp_pipeline.files_dicts = self.files_dicts
        self.nlp_pipeline.step2_extract_text_from_files()
        self.nlp_pipeline.step3_generate_vocabulary()
        vocabulary = [
            "falar",
            "é",
            "fácil",
            "mostre",
            "me",
            "o",
            "código",
            "escrever",
            "difícil",
            "que",
            "funcione",
        ]
        self.assertEqual(vocabulary, self.nlp_pipeline.vocabulary)

    def test_should_return_vocabulary_without_stopwords(self):
        self.nlp_pipeline = NLPPIpeline(
            self.files, _type='bow', log=True, with_vectors=False, stopwords=True
        )
        self.nlp_pipeline.files_dicts = self.files_dicts
        self.nlp_pipeline.step2_extract_text_from_files()
        self.nlp_pipeline.step3_generate_vocabulary()
        vocabulary = [
            'falar',
            'fácil',
            'mostre',
            'código',
            'escrever',
            'difícil',
            'funcione',
        ]
        self.assertEqual(vocabulary, self.nlp_pipeline.vocabulary)

    def test_should_return_2_grams_vocabulary(self):
        self.nlp_pipeline = NLPPIpeline(
            self.files, _type='2gram', log=True, with_vectors=False
        )
        self.nlp_pipeline.files_dicts = self.files_dicts
        self.nlp_pipeline.step2_extract_text_from_files()
        self.nlp_pipeline.step3_generate_vocabulary()
        vocabulary = [
            'falar é',
            'é fácil',
            'fácil mostreme',
            'mostreme o',
            'o código',
            'código é',
            'fácil escrever',
            'escrever código',
            'código difícil',
            'difícil é',
            'é escrever',
            'código que',
            'que funcione',
        ]
        self.assertEqual(vocabulary, self.nlp_pipeline.vocabulary)

    def test_should_return_vectors(self):
        self.nlp_pipeline = NLPPIpeline(
            self.files, _type='bow', log=True, with_vectors=True
        )
        self.nlp_pipeline.files_dicts = self.files_dicts
        self.nlp_pipeline.step2_extract_text_from_files()
        self.nlp_pipeline.step3_generate_vocabulary()
        self.nlp_pipeline.step4_generate_vectors()
        vectors = self.nlp_pipeline.vectors
        vector1 = vectors[0]['vector']
        vector2 = vectors[1]['vector']
        self.assertEqual(vector1, [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0])
        self.assertEqual(vector2, [0, 2, 1, 0, 0, 0, 2, 2, 1, 1, 1])

    def test_should_return_2grams_vectors(self):
        self.nlp_pipeline = NLPPIpeline(
            self.files, _type='2grams', log=True, with_vectors=True
        )
        self.nlp_pipeline.files_dicts = self.files_dicts
        self.nlp_pipeline.step2_extract_text_from_files()
        self.nlp_pipeline.step3_generate_vocabulary()
        self.nlp_pipeline.step4_generate_vectors()
        vectors = self.nlp_pipeline.vectors
        vector1 = vectors[0]['vector']
        vector2 = vectors[1]['vector']
        self.assertEqual(vector1, [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(vector2, [0, 1, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1])
