from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from app.api.viewsets import MultiSerializerMixin
from authors.api import serializers
from authors.models import Author

# Create your API views and viewsets here.


class AuthorsViewSet(MultiSerializerMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
