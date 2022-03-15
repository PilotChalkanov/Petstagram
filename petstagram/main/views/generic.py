from django.shortcuts import render

from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }

    return render(request, 'main/home_page.html', context)


def show_dashboard(request):
    profile = get_profile()

    pet_photos = PetPhoto.objects \
        .prefetch_related('tagged_pets').distinct()

    context = {
        'pet_photos': pet_photos,
    }

    return render(request, 'main/dashboard.html', context)