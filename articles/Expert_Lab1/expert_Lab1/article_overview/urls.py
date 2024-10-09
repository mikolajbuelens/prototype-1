from django.urls import path
from . import views


urlpatterns = [
# path('', views.main, name='main'),
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.loginInterfaceView.as_view() , name='login'),
    path('article_overview/', views.article_overview, name='article_overview'),
    path('article_overview/details/<int:id>/', views.details, name='details'),
    path('article/new', views.CreateArticleView.as_view(), name='article.create'),
]