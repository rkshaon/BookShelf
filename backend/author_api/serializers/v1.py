from rest_framework import serializers

from author_api.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id', 'full_name', 'biography', 'birth_date',
            'died_date', 'is_alive',
        ]
