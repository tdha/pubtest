import os
from openai import OpenAI
from dotenv import load_dotenv
from django.utils import timezone
from polls.models import Article

load_dotenv("pubtest/.env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found. Check your .env file.")

client = OpenAI(api_key=api_key)

def ask_chatgpt(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return "I couldn't fetch a response."

def generate_questions(article_id, headline, trail_text, body):
    formatted_prompt = (
        "You are a sociologist working to improve public policy. You are interested in the public opinion on current newsworthy topics.\n\n"
        "Write a one line summary of the provided article (do not prefix i.e. remove 'summary'; do not use periods mid-sentence; always end the sentence with a full stop), then write a yes/no question (do not prefix i.e. remove 'question') that, once presented to the general population, will result in insightful demographic data.\n\n"
        "News article below:\n\n"
        f"Headline: {headline}\n"
        f"Trail Text: {trail_text}\n"
        f"Body: {body}"
    )
    try:
        # Request the OpenAI API to generate a question
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": formatted_prompt}
            ]
        )
        # Extract the first and second sentences
        sentences = response.choices[0].message.content.split('.')
        summary = sentences[0].strip()
        question = sentences[1].strip()

        return summary, question
    
    except Exception as e:
        print(f"An error occurred while generating the question: {e}")
        return None, None

def save_generated_question(article_id, summary, question):
    try:
        # Retrieve the Article object by its ID
        article = Article.objects.get(id=article_id)
        
        # Update the summary and question fields
        article.summary = summary
        article.question = question
        
        # Save the changes to the database
        article.save()
        
        return True
    except Article.DoesNotExist:
        print("Article not found.")
        return False
    except Exception as e:
        print(f"An error occurred while saving generated question: {e}")
        return False
