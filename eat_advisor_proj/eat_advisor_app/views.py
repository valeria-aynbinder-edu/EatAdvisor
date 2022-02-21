import json

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core import serializers

from .models import Restaurant, Review
from .serializers import RestaurantSerializer, ReviewSerializer


@api_view(['GET', 'POST'])
def restaurants_list(request):
    if request.method == 'GET':
        all_restaurants = Restaurant.objects.all()
        #all_restaurants not json serializable
        # data = serializers.serialize("json", all_restaurants)
        # return Response(data)
        # return Response(json.loads(data))

        serializer = RestaurantSerializer(all_restaurants, many=True)
        print(serializer.data)
        return Response(serializer.data)

        # Q + tutorial: add filters

    elif request.method == 'POST':
        # new_rest = Restaurant(
        #     name=request.data['name'],
        #     country=request.data['country'],
        #     city=request.data['city'],
        #     type=request.data['type'],
        #     price_range=request.data['price_range']
        # )
        # new_rest.save()
        # return new_rest
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_details(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        rest = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantSerializer(rest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantSerializer(rest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # tutorial - add APIs for Reviews

@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def reviews(request):
    if request.method == 'GET':
        all_reviews = Review.objects.all()
        serializer = ReviewSerializer(all_reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)