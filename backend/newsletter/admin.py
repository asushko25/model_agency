from django.contrib import admin

from .models import NewsLetter, NewsLetterSubscriber


class NewsLetterSubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "subscribed_at",
        "is_active",
    )
    list_filter = (
        "is_active",
        "subscribed_at",
    )
    search_fields = ["email"]


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = (
        "header",
    )
    search_fields = ["header"]


# TODO: when creating newsletter subscriber using admin site
# TODO: we then need to specify in session email
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(NewsLetterSubscriber, NewsLetterSubscriberAdmin)
