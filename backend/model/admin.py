from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext as _

from .forms import UserCreationForm
from .models import Model, ModelImages, User


class ModelAdmin(admin.ModelAdmin):
    list_display = (
        "get_full_name",
        "country",
        "city",
        "height",
        "bust",
        "waist",
        "hips",
    )
    list_filter = (
        "country",
        "hair",
        "eye_color",
    )
    search_fields = ["model_user__full_name"]

    def get_full_name(self, obj):
        return obj.model_user.full_name

    get_full_name.short_description = "Full Name"


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "full_name",
                    "phone_number",
                ),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "full_name",
                )
            },
        ),
        (_("Permissions"), {"fields": ["is_active"]}),
        (_("Important dates"), {"fields": ["date_joined"]}),
    )
    list_display = (
        "full_name",
        "email",
        "phone_number",
        "is_staff",
    )
    search_fields = (
        "email",
        "full_name"
    )
    ordering = ("email",)


admin.site.register(Model, ModelAdmin)
admin.site.register(ModelImages)
