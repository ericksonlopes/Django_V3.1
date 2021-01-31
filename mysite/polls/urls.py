from django.urls import path

from . import views

urlpatterns = [
    # url e index da url
    path('', views.index, name='index'),
]
