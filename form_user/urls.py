# Django
from django.urls import path

# View
from .views import FormUserView


app_name = 'forms_users'

urlpatterns = [

    path(
        route='',
        view=FormUserView.as_view(),
        name='register'
    ),
]