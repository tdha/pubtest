import os
import requests
from django.utils import timezone
from polls.models import Article
from .gpt_api import generate_questions, save_generated_question
from django.db import IntegrityError

def fetch_articles(request):
    guardian_api_key = os.getenv('GUARDIAN_API_KEY')
    section = request.GET.get('section', 'australia-news')
    page_size = request.GET.get('page_size', 24)
    guardian_url = f"https://content.guardianapis.com/search?order-by=newest&section={section}&page-size={page_size}&show-fields=headline,trailText,body&api-key={guardian_api_key}"

    print(guardian_url)

    try:
        response = requests.get(guardian_url)
        response.raise_for_status() 
        data = response.json()

        articles = data['response']['results']
        formatted_data = []

        for article in articles:
            if (article.get('type') != 'liveblog' and 
                not article.get('webTitle', '').startswith('Morning Mail') and 
                not article.get('webTitle', '').startswith('Afternoon Update') and 
                not article.get('webTitle', '').startswith('Afternoon update')):

                # Create an Article (db) instance and populate fields
                new_article = Article(
                    web_url=article['webUrl'],
                    headline=article['fields']['headline'],
                    trail_text=article['fields']['trailText'],
                    body=article['fields']['body'],
                    date=timezone.now(),
                    summary='',  # Initialize summary as empty
                    question='',  # Initialize question as empty
                )

                try:
                    # Check if the article with the same web_url already exists in the database
                    existing_article = Article.objects.get(web_url=new_article.web_url)
                    print(f"Article with web_url {existing_article.web_url} already exists. Skipping.")
                except Article.DoesNotExist:
                    # If the article does not exist, save it to the database
                    new_article.save()
                    
                    # Pass the required arguments when calling generate_questions()
                    article_id = new_article.id
                    summary, question = generate_questions(article_id, new_article.headline, new_article.trail_text, new_article.body)
                    save_generated_question(article_id, summary, question)                

                formatted_data.append({
                    "web_url": new_article.web_url,
                    "headline": new_article.headline,
                    "trail_text": new_article.trail_text,
                    "body": new_article.body,
                })

        return formatted_data

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []
    except ValueError as e:
        print(f"JSON decoding error: {e}")
        return []
