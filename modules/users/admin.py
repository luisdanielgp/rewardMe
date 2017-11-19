from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from .models import User


class UserAdmin(UA):
    fieldsets = (
        ('account info', {
            'fields': ('email', 'password', 'is_active', 'is_staff')
        }), ('Personal info', {
            'fields': ('name', 'last_name1', 'last_name2', 'phone', 'gender')
        }),
        ('Groups', {
            'fields': ('groups',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'groups'),
        }),
    )

    def username(self, instance):
        return instance.email

    def user_first_name(self, instance):
        return instance.name

    def user_last_name(self, instance):
        return instance.last_name1

    list_display = ('email', 'name', 'last_name1', 'is_active', 'id')
    ordering = ('email',)


class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
