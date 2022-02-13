from django.shortcuts import render


def show_home(request):
    return render(request, 'home_page.html')

def show_dashboard(request):
    return render(request, 'dashboard.html')

def show_profile(request):
    return render(request,"profile_details.html")
