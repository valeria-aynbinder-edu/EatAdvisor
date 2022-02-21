import rest_framework.fields
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import CharField

from .models import Restaurant, Review



class RestaurantSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = CharField(required=True, max_length=128)
    country = CharField(required=True, max_length=128)
    city = CharField(required=True, max_length=128)
    address = CharField(required=False, max_length=128, allow_null=True)
    type = CharField(required=True, max_length=128)
    price_range = rest_framework.fields.IntegerField(required=True, min_value=1, max_value=3)
    pic_url = rest_framework.fields.URLField(required=False, allow_null=True)

    def create(self, validated_data):
        """
        Create and return a new `Restaurant` instance, given the validated data.
        """
        return Restaurant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.type = validated_data.get('type', instance.type)
        instance.price_range = validated_data.get('price_range', instance.price_range)
        instance.pic_url = validated_data.get('pic_url', instance.pic_url)
        instance.save()
        return instance


# class RestaurantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Restaurant
#         fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # depth = 1

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'