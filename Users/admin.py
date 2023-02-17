from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

from .admin_forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_filter = []
    list_display = ('email', 'first_name', 'last_name', 'address', 'number', 'age', 'job')
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'username')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'address', 'number', 'age', 'job')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password1', 'password2')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'address', 'number', 'age', 'job')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)



