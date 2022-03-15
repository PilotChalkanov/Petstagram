from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def contains_only_letters(value):
    if not all(ch.isalpha() for ch in value):
        raise ValidationError("Invalid name. Name must contain only letters.")

def validate_file_max_size_in_mb(max_size_mb):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size_mb * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size_mb))

    return validate


@deconstructible
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Date must be greater than {self.min_date}')


@deconstructible
class MaxDateValidator:
    def __init__(self, max_date):
        self.max_date = max_date

    def __call__(self, value):
        if self.max_date < value:
            raise ValidationError(f'Date must be earlier than {self.max_date}')