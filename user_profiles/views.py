from django.shortcuts import render


def user_profiles(request):
    # displays user profiles
    template = "user_profiles/user_profiles.html"
    context = {}

    return render(request, template, context)
