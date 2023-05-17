from django.shortcuts import get_list_or_404, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .serializers import MovieSerializer

from .models import Movie, Genre
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def Movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
