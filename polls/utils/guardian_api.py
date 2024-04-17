import os
import requests
from django.http import JsonResponse

def fetch_articles(request):
    guardian_api_key = os.getenv('GUARDIAN_API_KEY')
    section = request.GET.get('section', 'australia-news')
    page_size = request.GET.get('page_size', 10)
    guardian_url = f"https://content.guardianapis.com/search?order-by=newest&section={section}&page-size={page_size}&show-fields=headline,trailText,body&api-key={guardian_api_key}"

    try:
        response = requests.get(guardian_url)
        response.raise_for_status() 
        data = response.json()

        articles = data['response']['results']
        formatted_data = [
            {"headline": article['fields']['headline'],
             "trailText": article['fields']['trailText'],
             "body": article['fields']['body']}
            for article in articles
            if article.get('type') != 'liveblog' and
               not article.get('webTitle', '').startswith('Morning Mail:') # filter unwanted article types
        ]
        return formatted_data

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []
    except ValueError as e:
        print(f"JSON decoding error: {e}")
        return []
    