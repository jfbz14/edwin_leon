from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_global/admin/', admin.site.urls),
    path('', include(('form_user.urls'))),

]
