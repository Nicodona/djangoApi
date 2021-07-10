from django.shortcuts import render

from rest_framework import generics
from .serializers import BookSerializer
# from djangoApi.myproject.books.models import Book
from books.models import Book

class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer