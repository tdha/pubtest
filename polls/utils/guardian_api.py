# This is a simple modification to ensure it can be used directly as a Django view.
import os
import requests
from django.http import JsonResponse

def fetch_articles(request):
    guardian_api_key = os.getenv('GUARDIAN_API_KEY')
    section = request.GET.get('section', 'australia-news')
    page_size = request.GET.get('page_size', 3)

    guardian_api_key = os.getenv('GUARDIAN_API_KEY')
    guardian_url = f"https://content.guardianapis.com/search?order-by=newest&section={section}&page-size={page_size}&show-fields=headline,trailText&api-key={guardian_api_key}"

    try:
        response = requests.get(guardian_url)
        response.raise_for_status()  # ensures we raise an exception for bad responses
        data = response.json()
        return JsonResponse(data)  # Directly return the JSON data
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
