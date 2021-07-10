from django.shortcuts import render
from .models import Todo
from rest_framework import generics
from .serializers import TodoSerializers

# Create your views here.

class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailsList(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers