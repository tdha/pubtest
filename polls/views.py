from django.shortcuts import render
from .utils.guardian_api import fetch_articles
from .utils.gpt_api import generate_questions

temps = [
    {'summary':'A 16-year-old boy allegedly stabbed a bishop and others during a church service in Sydney, leading to a riot and violence towards police and paramedics', 'question':'Should public figures like Bishop Mar Mari Emmanuel be more cautious when discussing sensitive religious topics to prevent incidents like the Sydney church stabbing?'},
    {'question':'Six people were killed and 12 others injured in a mass stabbing at a shopping centre in Sydney.', 'question':'Should mental health support and resources be increased in communities to prevent similar tragic incidents from happening in the future?'},
]

def home(request):
    return render(request, 'home.html', {
        'temps': temps
    })

def index(request):
    return render(request, 'polls_index.html')

def about(request):
    return render(request, 'about.html')

def polls(request):
    articles = fetch_articles(request) 
    if not articles: 
        return render(request, 'polls.html', {'questions': ['No articles found.']})
    
    questions = [generate_questions(article) for article in articles]  
    return render(request, 'polls.html', {'questions': questions})