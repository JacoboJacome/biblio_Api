from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


from system_manage.serializers import CatalogSerializer
from .models import Book

class CatalogLibrary(ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','author','published','subject']

    @action(detail=True)
    def published_books(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = self.get_serializer_class()
        serializer = CatalogSerializer(books, many=True)
        return  Response(serializer.data, status=200)
