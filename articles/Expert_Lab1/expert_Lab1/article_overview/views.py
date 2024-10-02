from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article


# Create your views here.
def article_overview(request):
    articles = Article.objects.all().values()
    template = loader.get_template('articles.html')
    context = {
    'articles': articles,
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