from django.core.exceptions import ValidationError


def contains_only_letters(value):
    if not all(ch.isalpha() for ch in value):
        raise ValidationError("Invalid name. Name must contain only letters.")
