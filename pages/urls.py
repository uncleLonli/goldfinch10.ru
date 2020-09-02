from django.urls import path

from . import views

urlpatterns = [
    path ('', views.header),
    path ('work', views.content),
    path ('about', views.aboutpage),
]