from django.core.exceptions import ValidationError


def contains_only_letters(value):
    if not all(ch.isalpha() for ch in value):
        raise ValidationError("Invalid name. Name must contain only letters.")

def validate_file_max_size_in_mb(max_size_mb):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size_mb * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size_mb))

    return validate
