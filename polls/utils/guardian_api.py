import os
import requests
from django.http import JsonResponse

def fetch_articles(request):
    guardian_api_key = os.getenv('GUARDIAN_API_KEY')
    section = request.GET.get('section', 'australia-news')
    page_size = request.GET.get('page_size', 10)

    # Correct the URL by removing 'type' from show-fields
    guardian_url = f"https://content.guardianapis.com/search?order-by=newest&section={section}&page-size={page_size}&show-fields=headline,trailText,body&api-key={guardian_api_key}"

    try:
        response = requests.get(guardian_url)
        response.raise_for_status()  # Ensures we raise an exception for bad responses
        data = response.json()

        # Implement any needed filtering for 'type' within the Python code, not via the API URL
        articles = data['response']['results']
        filtered_articles = [
            article for article in articles
            if article.get('type') != 'liveblog' and
               not article.get('webTitle', '').startswith('Morning Mail:')
        ]

        # Update the data dictionary with filtered articles
        data['response']['results'] = filtered_articles

        return JsonResponse(data)  # Directly return the JSON data
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
