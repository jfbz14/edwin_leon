# Django
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

#mode
from .models import UserProfile


class UserProfileResource(resources.ModelResource):

    class Meta:
        model = UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    """UserProfile admin."""

    resource_class = UserProfileResource
    list_display = ('id', 'first_name', 'last_name', 'document_number', 'phone_number', 'email', )
    search_fields = ('document_number', 'first_name', )
    list_per_page = 25
