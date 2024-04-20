from django.shortcuts import render, redirect
from .utils.guardian_api import fetch_articles
from .utils.gpt_api import generate_questions
from .models import Article
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # 'user' form that includes data from the browser
        if form.is_valid():
            user = form.save()
            login(request, user) # logs in the user
            return redirect('index')
        else:
            error_message = "Unable to sign up. Please try again."
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)
