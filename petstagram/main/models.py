from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.main.validators import validate_contains_only_letters, validate_file_max_size_in_mb

"""
The user must provide the following information in their profile:
The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
Profile picture - the user can link their picture using a URL.

The user may provide the following information in their profile:
Date of birth: day, month, and year of birth.
Description - a user can write any description about themselves, no limit of words/chars.
Email - a user can only write a valid email address.
Gender - the user can choose one of the following: "Male", "Female", and "Do not show".
"""


class Profile(models.Model):

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    # Fields
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LEN), validate_contains_only_letters),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(MinLengthValidator(LAST_NAME_MIN_LEN), validate_contains_only_letters),
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(null=True, blank=True)

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "user_profiles"


class Pet(models.Model):

    # Constants
    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    # Fields(Columns)
    name = models.CharField(max_length=30, unique=True)
    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # relations
    user_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name} - {self.type}"

    class Meta:
        unique_together = ("user_id", "name")


class Photo(models.Model):

    photo = models.ImageField(
        validators=(
            validate_file_max_size_in_mb(5),
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )