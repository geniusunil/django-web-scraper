from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainscrap.urls')),
    path('',include('user.urls')),
]
