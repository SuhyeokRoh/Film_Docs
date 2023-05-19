from rest_framework import serializers
from .models import Movie, Review, Genre



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


# class MovieSerializer(serializers.ModelSerializer):
    
#     genres = GenreSerializer(many=True)
#     class Meta:
#         model = Movie
#         fields = "__all__"
class MovieSerializer(serializers.ModelSerializer):
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

        def to_representation(self, instance):
            return instance.name

    genres = GenreNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        # fields = "__all__"
        fields = ('content','movie')