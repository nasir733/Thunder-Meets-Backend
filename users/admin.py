from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User as Account
from django.utils.translation import gettext_lazy as _

# Register your models here.

class AccountAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password", "created")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "avatar","country")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    list_display = (
        "email",
        'id',
        "first_name",
        "last_name",
        "created",
        "is_staff",
        "avatar",
    )

    search_field = ("email", "first_name", "last_name")
    readonly_fields = (
        "id",
        "created",
    )


admin.site.register(
    Account,
    AccountAdmin,
)
