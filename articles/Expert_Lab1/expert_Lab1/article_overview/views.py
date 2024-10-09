from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy


# Note:Python is an MVT framework

# Create your views here.


# Examples of class-based views
class HomeView(CreateView):
     template_name = 'main.html'
     form_class = UserCreationForm
     succes_url = '/login'

     
    #  Trying to remove helper text (error: NoneType object is not subscriptable)
    #  class Meta:
    #     model = User
    #     fields = ['username', 'password1', 'password2']
    #  def __init__(self, *args, **kwargs):
    #   super().__init__(*args, **kwargs)
      
    
class ArticleView(TemplateView):
    template_name = 'articles.html'

class loginInterfaceView(LoginView):
    template_name = 'login.html'
    
    class logoutInterfaceView(LogoutView):
        template_name = 'main.html'
        
        
        # class ArticleContainerView(CreateView):
        #     model = Article
        #     fields = ['title', 'body', 'author']
        #     template_name = 'article_container.html'
        #     success_url = '/articles.html'
            
            
class CreateArticleView(CreateView):
    model = Article
    fields = ['title', 'body', 'author', 'image']
    template_name = 'create_article.html'
    success_url = '/article.overview/'
        
        
        

# class ArticleView(TemplateView):
#     template_name = 'articles.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         return context


# def login (request):
#     template = loader.get_template('login.html')
#     return HttpResponse(template.render({}, request))

# @login_required(login_url='/')




class ArticleContainerView(TemplateView):
    template_name = 'article_container.html'
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context

def article_overview(request):
    
    
    articles = Article.objects.all().values()
    data = Article.objects.filter(author__startswith='R').values()
    template = loader.get_template('articles.html')
    context = {
    'articles': articles,
    'data' : data,
}
    return HttpResponse(template.render(context, request))

def details(request, id):
    article = Article.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'article': article,
}
    return HttpResponse(template.render(context, request))

# def main(request):
#     template = loader.get_template('main.html')
#     return HttpResponse(template.render({}, request))