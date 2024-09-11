from rest_framework import serializers

from author_api.serializers.v1 import AuthorSerializer

from book_api.models import Genre
from book_api.models import Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['authors'] = AuthorSerializer(
            instance.authors, many=True).data

        return representation
