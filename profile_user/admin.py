# Django
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Model
from .models import User


admin.site.site_header = 'App Guiatec'
admin.site.index_title = 'App Guiatec'
admin.site.site_title = 'App Guiatec'


class UserResource(resources.ModelResource):

    class Meta:
        model = User


@admin.register(User)
class UserProfileAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    list_per_page = 25

