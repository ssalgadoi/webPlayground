from django.urls import path
from . import views

urlpatterns = [
    path('', wiews.home, name="home"),
    path('sample/', views.sample, name="sample")
]