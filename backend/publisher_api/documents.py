from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

from publisher_api.models import Publisher


publisher_index = Index('publishers')


@registry.register_document
class PublisherDocument(Document):
    class Index:
        name = 'publishers'

    class Django:
        model = Publisher
        fields = [
            'name',
        ]
