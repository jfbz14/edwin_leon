# Django
from django.urls import path

# View
from . import views


app_name = 'form_user'

urlpatterns = [

    path(
        route='',
        view=views.index,
        name='register'
    ),
]