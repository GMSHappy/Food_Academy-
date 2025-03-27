from django.contrib import admin
from .models import Module, Student


class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date")
    search_fields = ("title",)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "enrollment_date", "last_updated")
    search_fields = ("first_name", "last_name", "email")


admin.site.register(Module, ModuleAdmin)
admin.site.register(Student, StudentAdmin)
