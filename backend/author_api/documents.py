from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

from author_api.models import Author


author_index = Index('authors')


@registry.register_document
class AuthorDocument(Document):
    class Index:
        name = 'authors'

    class Django:
        model = Author
        fields = [
            'name',
        ]
