from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import ProfileForm, CustomAuthenticationForm
from .models import Article, Response, Profile
from .utils.guardian_api import fetch_articles

import logging

logger = logging.getLogger(__name__)

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

@login_required
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
            return redirect('home')
        else:
            error_message = "Unable to sign up. Please try again."
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)


def user_login(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            error_message = "Invalid username or password. Please try again."
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})


@login_required
@require_http_methods(["GET", "POST"])
def vote(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id') 
        answer = request.POST.get('answer')

        # Check if the article_id exists in the database
        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            return HttpResponse('Article does not exist', status=404)

        # Create a new response object and save it to the database
        response = Response.objects.create(answer=answer, user=request.user, article=article)

        # Redirect the user to the home page after voting
        return redirect('home')
    
    else: 
        return HttpResponse('GET request received.')


@login_required
def profile(request):
    try: 
        profile = Profile.objects.get(user=request.user) # check if user already has a profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile) # pass instance to updated existing profile
        if form.is_valid():
            profile = form.save(commit=False) # creates 'Profile' object (not saved to db)
            profile.user = request.user # set user field as current user
            profile.save()
            return redirect('home')
    
    else:
        form = ProfileForm(instance=profile) # if profile exists, populate form with existing profile data
    
    return render(request, 'profile.html', { 'form': form }) # renders web page