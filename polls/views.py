from django.shortcuts import render
from django.http import HttpResponse

from .utils.guardian_api import fetch_articles
import requests

def home(request):
    return render(request, 'home.html')

def index(request):
    # return HttpResponse("Hello, world. Polls in Pubtest.")
    return render(request, 'polls_index.html')

# def home(request):
#     if request.method == 'GET':
#         query = request.GET.get('query', 'news')
#         articles = fetch_articles(section=query)
#         print(query, articles)  # Debugging output
#         return render(request, 'home.html', {'data': articles})
#     else:
#         return render(request, 'home.html')
    
# def fetch_articles_from_guardian():
#     api_key = 'your_guardian_api_key'
#     page_size = 10
#     sections = 'australia-news'
#     content_type = 'article'
#     url = f"https://content.guardianapis.com/search?order-by=newest&section={sections}&page-size={page_size}&type={content_type}&show-fields=headline,trailText&api-key={api_key}"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         return response.json()['response']['results']
#     except requests.RequestException as e:
#         print(e)
#         return []

# def headlines_news(request):
#     articles = fetch_articles()  # Make sure this function returns the list of articles
#     return render(request, 'headlines_news.html', {'articles': articles})