# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from . import serializers
from rest_framework import viewsets
from rest_framework import status
from . import models
from rest_framework.authentication import TokenAuthentication
from .import permissions
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.

class HelloApiView(APIView):
    """Test API view."""

    serializer_class = serializers.HelloSerializer



    def get(self,request,format=None):
        """Returns a list of APIView features."""

        an_apiview = [
        'uses HTTP methods as function(get,post,patch)'
        ]

        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        """ create a hello message with our name."""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating an object"""

        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Patch request,only updates fields provided in the request"""

        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Delete the field"""

        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""


    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Returns a helo message."""
        a_viewset=['Uses action(list,create,retrieve,update,partial)']

        return Response({'messages':'Hello','_viewset':a_viewset})

    def create(self,request):
        """create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello{0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):

            """handles getting an object by its ID"""

            return Response({'http_method':'GET'})

    def update(self,request,pk=None):
            """handles updating an object"""

            return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
            """Handles updating part of an object"""

            return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
            """Handles removing an object."""

            return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles create,creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends =(filters.SearchFilter,)
    search_fields =('name','email',)

class LoginViewSet(viewsets.ViewSet):
    """checks email and password and returns an auth token."""

    serializer_class =
