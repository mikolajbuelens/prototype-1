from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
# path('', views.main, name='main'),
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.loginInterfaceView.as_view() , name='login'),
    path('article_overview/', views.article_overview, name='article_overview'),
    path('article_overview/details/<int:id>/', views.details, name='details'),
    path('article/new', views.CreateArticleView.as_view(), name='article.create'),
    path('logout/', views.LogoutPage.as_view(next_page="home"), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)