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

    def has_add_permission(self, request):
        """
        We do not want to let admins add newsletters
        subscribers, it will violate (GDPR)
        General Data Protection Regulation.
        f you add a subscriber manually via the admin panel,
        it will not be related to the actual user action, and
        usual session key and value will not be created.
        :param request:
        :return:
        """
        return False


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = (
        "header",
    )
    search_fields = ["header"]


# TODO: when creating newsletter subscriber using admin site
# TODO: we then need to specify in session email
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(NewsLetterSubscriber, NewsLetterSubscriberAdmin)
