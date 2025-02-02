from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from User.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'name', 'email', 'phone_number', 'is_staff', 'is_superuser', 'is_active')  # Show username
    list_display_links = ('name','username',)
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email', 'name']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
        }),
    )

admin.site.register(User, CustomUserAdmin)


