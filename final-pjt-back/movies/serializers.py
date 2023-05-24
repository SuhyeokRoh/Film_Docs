from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)
        
        
class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


class ProductionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Production
        fields = '__all__'
        
        
class MovieSerializer(serializers.ModelSerializer):

    class UserNameSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = 'username',
    
    movie_like_users = UserNameSerializer(many=True)
    movie_dislike_users = UserNameSerializer(many=True)
    genres = GenreSerializer(many=True)
    production_companies = ProductionSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = "__all__"
        

class CommentListSerializer(serializers.ModelSerializer):
    # 프로필에서 댓글을 보기 위해 추가
    # movie_title = serializers.ReadOnlyField(source='movie.title')
    # review_content = serializers.ReadOnlyField(source='review.content')

    class MovieAllAboutSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'


    class ReviewAllAboutSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = '__all__'


    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('username', 'nickname',)
            
    user = UserSerializer()
    movie = MovieAllAboutSerializer(read_only=True)
    review = ReviewAllAboutSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):

    class MovieAllSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    movie = MovieAllSerializer(read_only=True)
    comment_review = CommentListSerializer(many=True)
    
    class Meta:
        model = Review
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True)
    # 실험을 위한 장르 코드 삽입
    genres = GenreSerializer(many=True)
    production_companies = ProductionSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"
        

class ReviewCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'user_id',)
        

class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('username',)
    
    comment_review = CommentListSerializer(many=True)
    like_users = UserSerializer(many=True)
    dislike_users = UserSerializer(many=True)

    class Meta:
        model = Review
        fields = "__all__"
        

class CommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('content', 'movie', 'review', 'user_id',)
        

class CommentSerializer(serializers.ModelSerializer):
    # review_set = ReviewListSerializer(many=True)
    class Meta:
        model = Comment
        fields = "__all__"


class MoviechoiceSerializer(serializers.ModelSerializer):
   
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = "__all__"


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'movie', 'review', 'user_id',)
        
        
class WorldcupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ActorAllSerializer(serializers.ModelSerializer):
            
    movie_actor = MovieListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'
