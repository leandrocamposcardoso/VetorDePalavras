from rest_framework.response import Response
from rest_framework.views import APIView

from .nlp import NLPPIpeline


class FileVocabularyView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = NLPPIpeline(files_list, _type='bow', log=True, with_vectors=False)
        try:
            nlp.run()
            return Response(dict(vocabulary=nlp.vocabulary, words=len(nlp.vocabulary)))
        except Exception:
            return Response({'error': 'Ocorreu um erro'}, status=500)


class FileVectorView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = NLPPIpeline(files_list, _type='bow', log=True, with_vectors=True)
        try:
            nlp.run()
            return Response(nlp.vectors)
        except Exception:
            return Response({'error': 'Ocorreu um erro'}, status=500)


class FileTwoGramsVocabularyView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = NLPPIpeline(files_list, _type='2gram', log=True, with_vectors=False)
        try:
            nlp.run()
            return Response(dict(vocabulary=nlp.vocabulary, words=len(nlp.vocabulary)))
        except Exception:
            return Response({'error': 'Ocorreu um erro'}, status=500)


class FileTwoGramsVectorView(APIView):
    def post(self, request, *args, **kwargs):
        files_list = request.FILES
        nlp = NLPPIpeline(files_list, _type='2gram', log=True, with_vectors=True)
        try:
            nlp.run()
            return Response(nlp.vectors)
        except Exception:
            return Response({'error': 'Ocorreu um erro'}, status=500)
