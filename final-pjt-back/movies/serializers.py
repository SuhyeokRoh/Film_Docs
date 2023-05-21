from rest_framework import serializers
from .models import Movie, Review, Genre, Comment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)
        
        
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = "__all__"
        

class CommentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    comment_set = CommentListSerializer(many=True)
    
    class Meta:
        model = Review
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"
        

class ReviewCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'user_id',)
        

class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True)

    class Meta:
        model = Review
        fields = "__all__"
        

class CommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('content', 'movie', 'review', 'user_id',)
        

class CommentSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Comment
        fields = "__all__"