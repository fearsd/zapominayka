from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from app.api.viewsets import MultiSerializerMixin
from poems.api import serializers
from poems.models import Poem
from poems.models import Screen

# Create your API views and viewsets here.


class PoemsViewSet(MultiSerializerMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Poem.objects.all()
    serializer_class = serializers.PoemSerializer


class ScreensViewSet(MultiSerializerMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Screen.objects.all()
    serializer_class = serializers.ScreenSerializer
