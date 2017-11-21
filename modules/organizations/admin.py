from django.contrib import admin
from .models import Organization, Period, Goal

# Register your models here.


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'is_active']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Organization, OrganizationAdmin)


class PeriodAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


admin.site.register(Period, PeriodAdmin)


class GoalAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'organization', 'period']


admin.site.register(Goal, GoalAdmin)
