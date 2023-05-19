from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import ReviewListSerializer


class UserSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'last_name', 'first_name', 'email', 'nickname','review_set',)
        
