from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportMixin

from users.models import User
from core.models import Program, Indicator, DataElement, OrganizationUnit


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


class IndicatorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'program']


class DataElementAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'program']


class OrganizationUnitAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'code', 'name']


admin.site.register(User, UserAdmin)
admin.site.register(Program)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(DataElement, DataElementAdmin)
admin.site.register(OrganizationUnit, OrganizationUnitAdmin)

admin.site.site_header = 'ECHO SYSTEMS'
