from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

from book_api.models import Book


book_index = Index('books')


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
