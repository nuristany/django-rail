from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
        list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')

        add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "password1", "password2", "email", "phone",),
            },
        ),
    )
