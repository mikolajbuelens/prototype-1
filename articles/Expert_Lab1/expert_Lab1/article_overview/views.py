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
from django.contrib.auth.mixins import LoginRequiredMixin


# Note:Python is an MVT framework

# Create your views here.


# Examples of class-based views
class HomeView(CreateView):
     template_name = 'main.html'
     form_class = UserCreationForm
     success_url = '/article_overview'


class LogoutPage(LogoutView):
    template_name = 'logout.html'

      
    
class ArticleView(TemplateView):
    template_name = 'articles.html'

class loginInterfaceView(LoginView):
    template_name = 'login.html'
    
    # class logoutInterfaceView(LogoutView):
    #     template_name = 'main.html'
        
        
        # class ArticleContainerView(CreateView):
        #     model = Article
        #     fields = ['title', 'body', 'author']
        #     template_name = 'article_container.html'
        #     success_url = '/articles.html'
            
            
# @login_required
class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body', 'author', 'image', 'source']
    login_url = "/login"
    template_name = 'create_article.html'
    redirect_field_name = "redirect_to"
    # success_url = '/article_overview'

#         from django.contrib.auth.mixins import LoginRequiredMixin


# class MyView(LoginRequiredMixin, View):
#     login_url = "/login/"
#     redirect_field_name = "redirect_to"
        
        

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
    if request.user.is_authenticated:
        user = f'Welcome, {request.user}'
    else:
        user = ''
    
    template = loader.get_template('articles.html')
    context = {
    'articles': articles,
    'data' : data,
    'user': user,
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