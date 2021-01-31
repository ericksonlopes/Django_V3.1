from django.urls import path

from . import views

urlpatterns = [
    # url e index da url
    path('', views.index, name='index'),

    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.detail, name='results'),
    path('<int:question_id>/vote/', views.detail, name='vote')
]
