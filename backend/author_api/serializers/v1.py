from rest_framework import serializers

from author_api.models import Author
from book_api.models import Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = [
            'id', 'full_name', 'biography', 'birth_date',
            'died_date', 'is_alive', 'books',
        ]

    def get_books(self, obj):
        from book_api.serializers.v1 import BookSerializer

        if self.context.get('include_books', None):
            books = Book.objects.filter(authors=obj)
            return BookSerializer(books, many=True).data

        return None
