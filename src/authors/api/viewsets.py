from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from authors.api import serializers
from authors.models import Author
from app.api.viewsets import MultiSerializerMixin

# Create your API views and viewsets here.

class AuthorsViewSet(MultiSerializerMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
