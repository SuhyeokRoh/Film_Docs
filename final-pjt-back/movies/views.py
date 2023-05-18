from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MovieSerializer, MovieListSerializer, ReviewSerializer, ReviewListSerializer

from .models import Movie, Genre, Review
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_create(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        reviews = movie.review_set.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(username=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.objects(pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if not request.user.review_set.filter(pk=review_pk).exists():
            return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)