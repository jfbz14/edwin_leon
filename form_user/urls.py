# Django
from django.urls import path

# View
from .views import CreateFormUserProfileView, CreateFormUserLeaderView, TemplateHome


app_name = 'forms_users'

urlpatterns = [

    path(
        route='',
        view=CreateFormUserProfileView.as_view(),
        name='register'
    ),

    path(
        route='register/leader/',
        view=CreateFormUserLeaderView.as_view(),
        name='register_leader'
    ),

    path(
        route='home/',
        view=TemplateHome.as_view(),
        name='home'
    ),
]