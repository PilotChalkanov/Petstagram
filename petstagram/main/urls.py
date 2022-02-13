from django.urls import path

from petstagram.main.views import show_home, show_dashboard, show_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>/', show_profile, name='pet photo details'),

)
