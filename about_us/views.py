from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import About_us
from .forms import AboutUsForm


def about_us(request):
    main_mission = About_us.objects.filter(section=1)
    sub_mission = About_us.objects.filter(section=2)

    context = {
        "main_mission": main_mission,
        "sub_mission": sub_mission,
    }
    return render(request, "about_us/about_us.html", context)


@login_required
def append_about_us(request):
    # adds about us section
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("about_us"))

    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Mission statement section successfully added!")
            return redirect(reverse("append_about_us"))
        else:
            messages.error(request,
                           "Failed to add mission statement section. Please \
                                ensure the form is valid.")
    else:
        form = AboutUsForm()

    template = "about_us/append_about_us.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def change_about_us(request, about_us_id):
    # edits about us section
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("about_us"))

    about_us = get_object_or_404(About_us, pk=about_us_id)
    if request.method == "POST":
        form = AboutUsForm(
            request.POST, request.FILES, instance=about_us)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Mission statement section successfully updated!")
            return redirect(reverse("about_us"))
        else:
            messages.error(request, f'Failed to update the: "{about_us.title.title()}" section. \
                 Please ensure the form is valid.')
    else:
        form = AboutUsForm(instance=about_us)
        messages.info(
            request, f'You are editing the: "{about_us.title.title()}" \
            section.')

    template = "about_us/edit_about_us.html"
    context = {
        "form": form,
        "about_us": about_us,
    }

    return render(request, template, context)


@login_required
def remove_about_us(request, about_us_id):
    # deletes about us section
    if not request.user.is_superuser:
        messages.error(
            request, "Access Denied. \
                Access restricted to administrators only.")
        return redirect(reverse("about_us"))

    about_us = get_object_or_404(About_us, pk=about_us_id)
    about_us.delete()
    messages.success(request, "Mission statement section deleted!")

    return redirect(reverse("about_us"))
