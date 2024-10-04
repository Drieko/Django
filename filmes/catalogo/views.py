# catalogo/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Filme
from .serializers import FilmeSerializer

class FilmeList(APIView):
    def get(self, request):
        filmes = Filme.objects.all()
        serializer = FilmeSerializer(filmes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FilmeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilmeDetail(APIView):
    def get(self, request, pk):
        try:
            filme = Filme.objects.get(pk=pk)
            serializer = FilmeSerializer(filme)
            return Response(serializer.data)
        except Filme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            filme = Filme.objects.get(pk=pk)
            serializer = FilmeSerializer(filme, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Filme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            filme = Filme.objects.get(pk=pk)
            filme.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Filme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class FilmeByGenero(APIView):
    def get(self, request, genero):
        filmes = Filme.objects.filter(genero=genero)
        serializer = FilmeSerializer(filmes, many=True)
        return Response(serializer.data)

class FilmeDetail(APIView):
    def get(self, request, pk):
        try:
            filme = Filme.objects.get(pk=pk)
            serializer = FilmeSerializer(filme)
            return Response(serializer.data)
        except Filme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            filme = Filme.objects.get(pk=pk)
            serializer = FilmeSerializer(filme, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Filme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            filme = Filme.objects.get(pk=pk)
            filme.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Filme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)