from django.contrib import admin
from .models import About_us_section, About_us


class About_us_section_admin(admin.ModelAdmin):
    list_display = (
        "programmatic_name",
        "friendly_name",
    )


class About_us_admin(admin.ModelAdmin):
    list_display = (
        "title",
        "paragraph",
        "section",
        "image",
        "image_description",
    )


admin.site.register(About_us_section, About_us_section_admin)
admin.site.register(About_us, About_us_admin)
