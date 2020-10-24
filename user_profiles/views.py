from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfiles
from .forms import UserProfilesForm


def user_profiles(request):
    # displays user profiles
    user_profiles = get_object_or_404(UserProfiles, user=request.user)

    if request.method == 'POST':
        form = UserProfilesForm(request.POST, instance=user_profiles)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has successfully updated!")

    form = UserProfilesForm(instance=user_profiles)
    drink_orders = user_profiles.drink_orders.all()

    template = "user_profiles/user_profiles.html"
    context = {
        "form": form,
        "drink_orders": drink_orders,
    }

    return render(request, template, context)
