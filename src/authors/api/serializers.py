from rest_framework import serializers

# Create your DRF serializers here.
from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
