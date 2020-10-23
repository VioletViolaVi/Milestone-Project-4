from django.shortcuts import render, get_object_or_404

from .models import UserProfiles


def user_profiles(request):
    # displays user profiles
    user_profiles = get_object_or_404(UserProfiles, user=request.user)
    template = "user_profiles/user_profiles.html"
    context = {
        "user_profiles": user_profiles,
    }

    return render(request, template, context)
