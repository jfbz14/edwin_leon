# Django
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

#mode
from .models import *


class CommuneModelResource(resources.ModelResource):

    class Meta:
        model = CommuneModel


@admin.register(CommuneModel)
class CommuneModelAdmin(ImportExportModelAdmin):
    """CommuneModel admin."""

    resource_class = CommuneModelResource
    list_display = ('id', 'name_communa', )
    search_fields = ('name_communa', )
    list_per_page = 25


class NeighborhoodModelResource(resources.ModelResource):

    class Meta:
        model = NeighborhoodModel


@admin.register(NeighborhoodModel)
class NeighborhoodModelAdmin(ImportExportModelAdmin):
    """NeighborhoodModel admin."""

    resource_class = NeighborhoodModelResource
    list_display = ('id', 'name_communa', 'name_neighborhood',)
    search_fields = ('name_communa', 'name_neighborhood',)
    list_per_page = 25


class UserLeaderResource(resources.ModelResource):

    class Meta:
        model = UserLeader


@admin.register(UserLeader)
class UserLeaderAdmin(ImportExportModelAdmin):
    """UserLeader admin."""

    resource_class = UserLeaderResource
    list_display = ('id', 'first_name', 'last_name', 'document_number', 'phone_number', 'email', )
    search_fields = ('document_number', 'first_name', )
    list_per_page = 25


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
