from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article
from django.contrib.auth.decorators import login_required

# Note:Python is an MVT framework

# Create your views here.

@login_required
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

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))