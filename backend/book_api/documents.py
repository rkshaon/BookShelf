from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry

from book_api.models import Book
from book_api.models import Genre
from book_api.models import Topic
# from publisher_api.models import Publisher
# from author_api.models import Author


book_index = Index('books')
genre_index = Index('genres')
topic_index = Index('topics')


@registry.register_document
class BookDocument(Document):
    title = fields.TextField()
    book_code = fields.TextField()
    authors = fields.NestedField(properties={
        'full_name': fields.TextField(),
    })
    genres = fields.NestedField(properties={
        'name': fields.TextField(),
    })
    topics = fields.NestedField(properties={
        'name': fields.TextField(),
    })

    class Index:
        name = 'books'

    class Django:
        model = Book
        fields = [
            # 'title',
            'published_year',
        ]
        # related_models = [
        #     Author, Publisher, Genre, Topic,
        # ]
        related_models = [
            'author_api.Author',
            'publisher_api.Publisher',
            'book_api.Genre',
            'book_api.Topic',
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
