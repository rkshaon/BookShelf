from django.core.exceptions import ValidationError
import re


def validate_no_spaces(value):
    if not re.match(r'^[\w]+$', value):
        raise ValidationError(
            'The name must be a single word with no spaces. Only underscores (_) are allowed.'  # noqa
        )
