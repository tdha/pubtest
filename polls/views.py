from django.shortcuts import render
from .utils.guardian_api import fetch_articles  # Ensure this import is correct

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'polls_index.html')
