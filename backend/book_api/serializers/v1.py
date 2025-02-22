from rest_framework import serializers

from author_api.serializers.v1 import AuthorSerializer
from publisher_api.serializers.v1 import PublisherSerializer

from book_api.models import Genre
from book_api.models import Topic
from book_api.models import Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id', 'book_code', 'title', 'description', 'edition',
            'isbn', 'pages', 'published_year', 'language', 'book',
            'cover_image', 'publisher', 'genres', 'topics', 'authors',
            'added_by',
        ]

    def to_internal_value(self, data):
        if data.get('published_year') == "":
            data['published_year'] = None

        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['authors'] = AuthorSerializer(
            instance.authors, many=True
        ).data
        representation['genres'] = GenreSerializer(
            instance.genres, many=True
        ).data
        representation['topics'] = TopicSerializer(
            instance.topics, many=True
        ).data
        if instance.publisher:
            representation['publisher'] = PublisherSerializer(
                instance.publisher
            ).data
        if instance.cover_image:
            representation['cover_image'] = instance.cover_image.url

        return representation
