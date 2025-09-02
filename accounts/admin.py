# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # This decides what columns show up in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # These fields are clickable (links to detail view)
    list_display_links = ('username', 'email')

    # Add search bar support
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Filters on the right side
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Keep fieldsets same as Django’s default UserAdmin
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


# Register your CustomUser with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
