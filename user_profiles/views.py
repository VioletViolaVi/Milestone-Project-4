from django.shortcuts import render, get_object_or_404

from .models import UserProfiles
from .forms import UserProfilesForm


def user_profiles(request):
    # displays user profiles
    user_profiles = get_object_or_404(UserProfiles, user=request.user)

    form = UserProfilesForm(instance=user_profiles)
    drink_orders = user_profiles.drink_orders.all()

    template = "user_profiles/user_profiles.html"
    context = {
        "form": form,
        "drink_orders": drink_orders,
    }

    return render(request, template, context)
