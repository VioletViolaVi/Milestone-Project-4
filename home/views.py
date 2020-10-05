from django.shortcuts import render


def home(request):
    # shows homepage
    return render(request, "home/index.html")
