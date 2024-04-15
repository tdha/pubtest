from django.shortcuts import render
from .utils.guardian_api import fetch_articles
from .utils.gpt_api import generate_questions

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'polls_index.html')

def polls(request):
    articles = fetch_articles(request) 
    if not articles: 
        return render(request, 'polls.html', {'questions': ['No articles found.']})
    
    questions = [generate_questions(article) for article in articles]  
    return render(request, 'polls.html', {'questions': questions})