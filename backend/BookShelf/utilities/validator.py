from django.core.exceptions import ValidationError
import re


def validate_no_spaces(value):
    if not re.match(r'^[\w]+$', value):
        raise ValidationError(
            'The name must be a single word with no spaces. Only underscores (_) are allowed.'  # noqa
        )


def validate_book_file_type(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

    # if file.content_type != 'application/pdf':
    #     raise ValidationError('The uploaded file must be a valid PDF.')
