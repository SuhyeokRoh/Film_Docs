from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import *

from .models import Movie, Genre, Review
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
import random

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


@api_view(['POST'])
def movie_dislike(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.movie_dislike_users.filter(pk=request.user.pk).exists():
        movie.movie_dislike_users.remove(request.user)
    else:
        movie.movie_dislike_users.add(request.user)
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
    review = movie.review_set.filter(pk=review_pk)[0]
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
    
    

@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)      
    return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
@api_view(['PUT', 'DELETE'])
def review_update(request, movie_pk, review_pk):
    # movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review,pk=review_pk)
    # review = movie.review_set.filter(pk=review_pk)[0]
    if review.user_id != request.user.pk:
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    else:
        if request.method == 'PUT':
            # if review.user_id != request.user.pk:
            #     return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
            serializer = ReviewCreateSerializer(review, data=request.data)
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
    print(review)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    serialzer = ReviewSerializer(review)
    return Response(serialzer.data)


@api_view(['POST'])
def review_dislike(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.filter(pk=review_pk)[0]
    if review.dislike_users.filter(pk=request.user.pk).exists():
        review.dislike_users.remove(request.user)
    else:
        review.dislike_users.add(request.user)
    serialzer = ReviewSerializer(review)
    return Response(serialzer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def commentList(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.filter(pk=review_pk)[0]
    comments = review.comment_review.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def comment_create(request, movie_pk, review_pk):
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)     
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update(request, movie_pk, review_pk, comment_pk):
    # movie = get_object_or_404(Movie, pk=movie_pk)
    # review = movie.review_set.filter(pk=review_pk)[0]
    # print(review)
    # comment = review.comment_review.filter(pk=comment_pk)[0]
    comment = get_object_or_404(Comment,pk=comment_pk)
    # if not request.user.comment_set.filter(pk=review_pk).exists():
    #     return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    # else:
    #     if request.method == 'PUT':
    if comment.user_id != request.user.pk:
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    else:
        if request.method == 'PUT':
            # if not request.user.comment_set.filter(pk=review_pk).exists():
            #     return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
            serializer = CommentUpdateSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            comment.delete()
            return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)  

@api_view(['GET'])
@permission_classes([AllowAny])
def comment_detail(request, movie_pk, review_pk, comment_pk):
   
    comment = get_object_or_404(Comment,pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

# @api_view(['POST'])
# def comment_like(request, movie_pk, review_pk, comment_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     review = movie.review_set.filter(pk=review_pk)[0]
#     comment = review.comment_review.filter(pk=comment_pk)[0]
#     if comment.like_comment_users.filter(pk=request.user.pk).exists():
#         comment.like_comment_users.remove(request.user)
#     else:
#         comment.like_comment_users.add(request.user)
#     serialzer = CommentSerializer(comment)
#     return Response(serialzer.data)
@api_view(['POST'])
def comment_like(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if comment.like_comment_users.filter(pk=request.user.pk).exists():
        comment.like_comment_users.remove(request.user)
    else:
        comment.like_comment_users.add(request.user)
    serialzer = CommentSerializer(comment)
    return Response(serialzer.data)


# @api_view(['POST'])
# def comment_dislike(request, movie_pk, review_pk, comment_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     review = movie.review_set.filter(pk=review_pk)[0]
#     comment = review.comment_review.filter(pk=comment_pk)[0]
#     if comment.dislike_comment_users.filter(pk=request.user.pk).exists():
#         comment.dislike_comment_users.remove(request.user)
#     else:
#         comment.dislike_comment_users.add(request.user)
#     serialzer = CommentSerializer(comment)
#     return Response(serialzer.data)
@api_view(['POST'])
def comment_dislike(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if comment.dislike_comment_users.filter(pk=request.user.pk).exists():
        comment.dislike_comment_users.remove(request.user)
    else:
        comment.dislike_comment_users.add(request.user)
    serialzer = CommentSerializer(comment)
    return Response(serialzer.data)


@api_view(['GET'])
def movie_recommend(request):
    movies = get_list_or_404(Movie)

    random_movies = movies
    high_vote_rate_movies = sorted(movies, key=lambda x: x.vote_average, reverse=True)[:5]
    high_popularity_movies = sorted(movies, key=lambda x: x.popularity, reverse=True)[:5]
    high_like_movies = sorted(movies, key=lambda x: (x.movie_like_users.count(), x.vote_average, x.popularity), reverse=True)[:5]
    high_dislike_movies = sorted(movies, key=lambda x: (x.movie_dislike_users.count(), -x.vote_average, -x.popularity), reverse=True)[:5]

    data = {
    'random_movies': MovieListSerializer(random_movies, many=True).data,
    'high_vote_rate_movies': MovieListSerializer(high_vote_rate_movies, many=True).data,
    'high_popularity_movies': MovieListSerializer(high_popularity_movies, many=True).data,
    'high_like_movies': MovieListSerializer(high_like_movies, many=True).data,
    'high_dislike_movies': MovieListSerializer(high_dislike_movies, many=True).data,
    }

    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_release_list(request):
    movies = get_list_or_404(Movie)
    latest_release_date_movies = sorted(movies, key=lambda x: x.release_date, reverse=True)[:10]
    serializer = MovieListSerializer(latest_release_date_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
# def movie_choice(request, name):
def movie_choice(request):
    # genre=get_object_or_404(Genre, name=request.data)
    # movies = get_list_or_404(Movie,genres=genre)
    selected_genres = request.GET.getlist('genres')
    selected_genres = selected_genres[0].split(',')
    # print(selected_genres)
    movies = Movie.objects.filter(genres__name__in=selected_genres).distinct()
    # print(movies)
    # # movie = get_object_or_404(Genre, name=name)
    serializers = MoviechoiceSerializer(movies, many=True)
    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_search(request):
    movies = get_list_or_404(Movie)
    search_movie = request.GET.getlist('searchcontentlist')
    # search_movie가 장르에 들어옴. 
    # print(search_movie)
    search_result_movies = []
    for movie in movies:
        # print(movie.title)
        for i in range(len(search_movie)):
            if search_movie[i] in movie.title:
                search_result_movies.append(movie)
            # for j in search_movie[i]:
            #     if j in movie.title:
            #         search_result_movies.append(movie)
    if search_result_movies == []:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializers = MovieListSerializer(search_result_movies, many=True)
    return Response(serializers.data)

# 월드컵!
@api_view(['GET'])
def movie_worldcup(request):
    random_movies = random.sample(list(Movie.objects.all()), 8)
    worldcup = Worldcup()
    worldcup.save()
    worldcup.movies.set(random_movies)
    # worldcup = Worldcup.create(random_movies)
    worldcup_serializer = WorldcupSerializer(worldcup)
    return Response(worldcup_serializer.data)

@api_view(['GET'])
def worldcup_detail(request, worldcup_pk):
    worldcup = get_object_or_404(Worldcup, pk=worldcup_pk)
    worldcup_serializer = WorldcupSerializer(worldcup)
    return Response(worldcup_serializer.data)

@api_view(['POST'])
def create_worldcup(request):
    serializer = WorldcupSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)