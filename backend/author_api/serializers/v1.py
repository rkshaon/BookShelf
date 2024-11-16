from rest_framework import serializers

from author_api.models import Author
from book_api.models import Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = [
            'id', 'full_name', 'first_name', 'middle_name',
            'last_name', 'biography', 'birth_date',
            'died_date', 'is_alive', 'books', 'added_by',
        ]

    def to_internal_value(self, data):
        if data.get('birth_date') == "":
            data['birth_date'] = None
        if data.get('died_date') == "":
            data['died_date'] = None
        return super().to_internal_value(data)

    def validate(self, data):
        if (
            not data.get('first_name')
            and not data.get('middle_name')
            and not data.get('last_name')
        ):
            raise serializers.ValidationError(
                "Full name can not be empty!"
            )
        return data

    def get_books(self, obj):
        from book_api.serializers.v1 import BookSerializer

        if self.context.get('include_books', None):
            books = Book.objects.filter(authors=obj)
            return BookSerializer(books, many=True).data

        return None
