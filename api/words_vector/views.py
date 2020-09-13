from rest_framework.response import Response
from rest_framework.views import APIView

from .nlp import FileNlpPipeline


class FileVocabularyView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = FileNlpPipeline(files_list)
        nlp.step1_files_to_dicts()
        nlp.step2_get_files_words()
        nlp.step3_gen_vocabulary()
        nlp.step4_gen_vectors()
        nlp.save_logs()
        return Response(dict(vocabulary=nlp.vocabulary, words=len(nlp.vocabulary)))


class FileVectorView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = FileNlpPipeline(files_list)
        nlp.step1_files_to_dicts()
        nlp.step2_get_files_words()
        nlp.step3_gen_vocabulary()
        nlp.step4_gen_vectors()
        nlp.save_logs()
        return Response(nlp.vectors)


class FileTwoGramsVocabularyView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = FileNlpPipeline(files_list)
        nlp.step1_files_to_dicts()
        nlp.step2_get_files_words()
        nlp.step3_gen_two_grams_vocabulary()
        nlp.step4_gen_two_grams_vectors()
        nlp.save_logs()
        return Response(dict(vocabulary=nlp.vocabulary, words=len(nlp.vocabulary)))


class FileTwoGramsVectorView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = FileNlpPipeline(files_list)
        nlp.step1_files_to_dicts()
        nlp.step2_get_files_words()
        nlp.step3_gen_two_grams_vocabulary()
        nlp.step4_gen_two_grams_vectors()
        nlp.save_logs()
        return Response(nlp.vectors)
