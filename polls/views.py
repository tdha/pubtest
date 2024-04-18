from django.shortcuts import render
from .utils.guardian_api import fetch_articles
from .utils.gpt_api import generate_questions
from .models import Article

def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)

def index(request):
    return render(request, 'polls_index.html')

def about(request):
    return render(request, 'about.html')

def polls(request):
    articles = fetch_articles(request)
    if not articles:
        return render(request, 'polls.html', {'articles': [{'headline': 'No articles found.', 'trail_text': '', 'web_url': '#'}]})

    # Creating a list of dictionaries for each article, extracting web_url, headline, and trail_text
    article_data = [
        {'web_url': article.get('web_url', '#'), 'headline': article.get('headline', 'No headline available'), 'trail_text': article.get('trail_text', 'No trail text available')}
        for article in articles
    ]
    return render(request, 'polls.html', {'articles': article_data})