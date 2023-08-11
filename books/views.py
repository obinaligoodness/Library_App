from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, ReviewModel, BookInstance
from .serializers import BookSerializer, CreateBookSerializer, AuthorSerializer, CreateAuthorSerializer, \
    ReviewSerializer, BookInstanceSerializer

users = [
    {"name": "sheriff"},
    {"name": "Ned"},
    {"name": "sher"},
]


# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.select_related('author').all()
#         serializer = BookSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateBookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# # Create your views here.
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = CreateBookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         query_set = Author.objects.all()
#         serializer = AuthorSerializer(query_set, many=True, context={'request': request})
#         return Response(serializer.data, status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     if request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.request.data.get('author_id')
        if author_id is not None:
            queryset = Book.objects.filter(author_id=author_id)
            return queryset

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
