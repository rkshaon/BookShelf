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

    def update(self, instance, validated_data):
        """
        Handle updating many-to-many fields (authors, genres, topics)
        """
        if 'authors' in validated_data:
            instance.authors.set(validated_data['authors'])
        if 'genres' in validated_data:
            instance.genres.set(validated_data['genres'])
        if 'topics' in validated_data:
            instance.topics.set(validated_data['topics'])

        for attr, value in validated_data.items():
            if attr not in ['authors', 'genres', 'topics']:
                setattr(instance, attr, value)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['authors'] = AuthorSerializer(instance.authors, many=True).data  # noqa
        representation['genres'] = GenreSerializer(instance.genres, many=True).data     # noqa
        representation['topics'] = TopicSerializer(instance.topics, many=True).data     # noqa

        if instance.publisher:
            representation['publisher'] = PublisherSerializer(instance.publisher).data  # noqa

        if instance.cover_image:
            representation['cover_image'] = instance.cover_image.url

        return representation
