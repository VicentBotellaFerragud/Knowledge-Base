from django.shortcuts import render, redirect
from .models import Article
from .forms import NewArticleForm
from django.db.models import Q


def home(request):
    articles = Article.objects.all()
    search_made = False

    if request.method == 'GET':
        query = request.GET.get('search')

        if query:
            search_made = True
            articles = Article.objects.filter(
                Q(title__contains=query) | Q(text__contains=query))

    return render(request, 'home.html', {'articles': articles, 'search_made': search_made})


def add_article(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    form = NewArticleForm()

    return render(request, 'add-article.html')


def gtc(request):
    return render(request, 'gtc.html')


def imprint(request):
    return render(request, 'imprint.html')
