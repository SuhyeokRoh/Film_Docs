from rest_framework import serializers
from .models import Movie, Review, Genre, Comment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = "__all__"


class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    # comment = CommentListSerializer(many=True)

    class Meta:
        model = Review
        # fields = "__all__"
        fields = ('title', 'content', 'movie', 'user_id',)
        # read_only_fields = ('comment', 'like_users', 'dislike_users',)
        

class ReviewLikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'