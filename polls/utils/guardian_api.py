import os
import requests
from django.http import JsonResponse

def fetch_articles(request):
    section = request.GET.get('section', 'australia-news')
    page_size = request.GET.get('page_size', 3)

    guardian_api_key = os.getenv('GUARDIAN_API_KEY')
    guardian_url = f"https://content.guardianapis.com/search?order-by=newest&section={section}&page-size={page_size}&show-fields=headline,trailText,body&api-key={guardian_api_key}"

    try:
        response = requests.get(guardian_url)
        response.raise_for_status()
        data = response.json()
        print(data)  # Print JSON data for debugging

        return JsonResponse({
            'articles': data.get('response', {}).get('results', []),
            'error': None
        })
    except requests.RequestException as e:
        return JsonResponse({
            'articles': [],
            'error': str(e)
        })
