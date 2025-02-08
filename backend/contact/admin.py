from django.contrib import admin

from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    search_fields = ("name", "last_name", "email")
    list_display = (
        "full_name",
        "email",
        "phone_number",
        "model",
        "message",
        "created_at",
    )

    def full_name(self, obj):
        return obj.full_name


admin.site.register(Contact, ContactAdmin)
