from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

from book_api.models import Book
from book_api.models import Genre
from book_api.models import Topic


book_index = Index('books')
genre_index = Index('genres')
topic_index = Index('topics')


@registry.register_document
class BookDocument(Document):
    class Index:
        name = 'books'

    class Django:
        model = Book
        fields = [
            'title',
            'published_year',
        ]
        related_models = [
            'Author', 'Publisher', 'Genre', 'Topic',
        ]


@registry.register_document
class GenreDocument(Document):
    class Index:
        name = 'genres'

    class Django:
        model = Genre
        fields = [
            'name',
        ]


@registry.register_document
class TopicDocument(Document):
    class Index:
        name = 'topics'

    class Django:
        model = Topic
        fields = [
            'name'
        ]
