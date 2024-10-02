from django.urls import path
from . import views

urlpatterns = [
path('', views.main, name='main'),
    path('article_overview/', views.article_overview, name='article_overview'),
    path('article_overview/details/<int:id>/', views.details, name='details'),
]