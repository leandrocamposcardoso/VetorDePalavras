from rest_framework.response import Response
from rest_framework.views import APIView

from .nlp import NLPPIpeline


class FileVocabularyView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = NLPPIpeline(files_list, _type='bow', log=True, with_vectors=False)
        nlp.run()
        return Response(dict(vocabulary=nlp.vocabulary, words=len(nlp.vocabulary)))


class FileVectorView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = NLPPIpeline(files_list, _type='bow', log=True, with_vectors=True)
        nlp.run()
        return Response(nlp.vectors)


class FileTwoGramsVocabularyView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = NLPPIpeline(files_list, _type='2gram', log=True, with_vectors=False)
        nlp.run()
        return Response(dict(vocabulary=nlp.vocabulary, words=len(nlp.vocabulary)))


class FileTwoGramsVectorView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = NLPPIpeline(files_list, _type='2gram', log=True, with_vectors=True)
        nlp.run()
        return Response(nlp.vectors)
