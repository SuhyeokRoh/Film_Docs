from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MovieSerializer, MovieListSerializer, ReviewSerializer, ReviewListSerializer, CommentListSerializer, CommentSerializer, ReviewLikeSerializer

from .models import Movie, Genre, Review
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.movie_like_users.filter(pk=request.user.pk).exists():
        movie.movie_like_users.remove(request.user)
    else:
        movie.movie_like_users.add(request.user)
    serialzer = MovieSerializer(movie)
    return Response(serialzer.data)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def reviewList(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.objects(pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
    
    

@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)      
    return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
@api_view(['PUT', 'DELETE'])
def review_update(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.objects(pk=review_pk)

    if request.method == 'PUT':
        if not request.user.review_set.filter(pk=review_pk).exists():
            return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def review_like(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.filter(pk=review_pk)[0]
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    serialzer = ReviewLikeSerializer(review)
    return Response(serialzer.data)


@api_view(['POST'])
def review_dislike(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.filter(pk=review_pk)[0]
    if review.dislike_users.filter(pk=request.user.pk).exists():
        review.dislike_users.remove(request.user)
    else:
        review.dislike_users.add(request.user)
    serialzer = ReviewLikeSerializer(review)
    return Response(serialzer.data)


@api_view(['POST'])
def comment_create(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.filter(pk=review_pk)[0]
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)      
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update(request, movie_pk, review_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.filter(pk=review_pk)[0]
    comment = review.comment_set.filter(pk=comment_pk)[0]

    if request.method == 'PUT':
        if not request.user.comment_set.filter(pk=review_pk).exists():
            return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
        serializer = CommentSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)  


@api_view(['POST'])
def comment_like(request, movie_pk, review_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.filter(pk=review_pk)[0]
    comment = review.comment_set.filter(pk=comment_pk)[0]
    if comment.like_comment_users.filter(pk=request.user.pk).exists():
        review.like_comment_users.remove(request.user)
    else:
        review.like_comment_users.add(request.user)
    serialzer = CommentSerializer(review)
    return Response(serialzer.data)


@api_view(['POST'])
def comment_dislike(request, movie_pk, review_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.filter(pk=review_pk)[0]
    comment = review.comment_set.filter(pk=comment_pk)[0]
    if comment.dislike_comment_users.filter(pk=request.user.pk).exists():
        review.dislike_comment_users.remove(request.user)
    else:
        review.dislike_comment_users.add(request.user)
    serialzer = CommentSerializer(review)
    return Response(serialzer.data)