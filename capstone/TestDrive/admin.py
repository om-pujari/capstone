from django.contrib import admin
from .models import TestDrive

# Register your models here.

@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ['user', 'bike', 'test_drive_date', 'status']
    list_filter = ['status', 'test_drive_date']
    actions = ['approve_test_drives']

    def approve_test_drives(self, request, queryset):
        queryset.update(status='Approved')
    approve_test_drives.short_description = "Approve selected test drives"



