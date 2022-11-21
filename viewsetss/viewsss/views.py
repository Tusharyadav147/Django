from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many = True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data)
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk = None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = BookSerializer(user)
        return Response(serializer.data)
        