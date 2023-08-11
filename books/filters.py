from django_filters.rest_framework import FilterSet

from .models import Book


class CustomFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'author_id': ['exact'],
            'title': ['exact'],
            'copies': ['gt', 'lt']
        }
