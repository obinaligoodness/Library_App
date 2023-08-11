from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .filters import CustomFilter
from .models import Author, Book, ReviewModel, BookInstance
from .serializers import BookSerializer, CreateBookSerializer, AuthorSerializer, CreateAuthorSerializer, \
    ReviewSerializer, BookInstanceSerializer

users = [
    {"name": "sheriff"},
    {"name": "Ned"},
    {"name": "sher"},
]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CustomFilter
    search_fields = ['isbn', 'genre']
    ordering_fields = ['title']

    # def get_queryset(self):
    #     queryset = Book.objects.all()
    #     author_id = self.request.data.get('author_id')
    #     if author_id is not None:
    #         queryset = Book.objects.filter(author_id=author_id)
    #         return queryset

    def get_serializer_context(self):
        return {'request': self.request}


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ReviewViewSet(ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer


class BookInstanceAPIView(ListCreateAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
