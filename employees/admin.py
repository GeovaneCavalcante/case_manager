from django.contrib import admin

from .models import Employee, EmployeeFileImport


class BaseEmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'register_number',
                    'cpf', 'birth_date', 'is_active')
    search_fields = ('full_name', 'register_number', 'cpf')
    list_filter = ('is_active',)


admin.site.register(Employee, BaseEmployeeAdmin)
admin.site.register(EmployeeFileImport)
