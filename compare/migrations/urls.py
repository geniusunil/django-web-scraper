from django.urls import path
from . import views

urlpatterns = [
    path('compare', views.comp, name="compare"),
]
