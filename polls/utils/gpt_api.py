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

# def generate_questions(article_data):
#     formatted_prompt = (
#         "You are a sociologist working to improve public policy. You are interested in the public opinion on current newsworthy topics.\n\n"
#         "Write a one line summary of the provided article (do not prefix i.e. remove 'summary'; do not use periods mid-sentence; always end the sentence with a full stop), then write a yes/no question (do not prefix i.e. remove 'question') that, once presented to the general population, will result in insightful demographic data.\n\n"
#         "News article below:\n\n"
#         f"Headline: {article_data['headline']}\n"
#         f"Trail Text: {article_data['trail_text']}\n"
#         f"Body: {article_data['body']}"
#     )
#     try:
#         # Request the OpenAI API to generate a question
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": formatted_prompt}
#             ]
#         )
#         # Extract and return the generated question
#         return response.choices[0].message.content
#     except Exception as e:
#         print(f"An error occurred while generating the question: {e}")
#         return "I couldn't generate a question."

def generate_questions(article_data):
    formatted_prompt = (
        "You are a sociologist working to improve public policy. You are interested in the public opinion on current newsworthy topics.\n\n"
        "Write a one line summary of the provided article (do not prefix i.e. remove 'summary'; do not use periods mid-sentence; always end the sentence with a full stop), then write a yes/no question (do not prefix i.e. remove 'question') that, once presented to the general population, will result in insightful demographic data.\n\n"
        "News article below:\n\n"
        f"Headline: {article_data['headline']}\n"
        f"Trail Text: {article_data['trail_text']}\n"
        f"Body: {article_data['body']}"
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

        # print(summary)
        # print(question)
        
        return summary, question
    except Exception as e:
        print(f"An error occurred while generating the question: {e}")
        return None, None


# def save_generated_question(article_id, article_data, summary):
#     try:
#         question = generate_questions(article_data)

#         new_article = Article(
#             guardian_article_id=article_id,
#             web_url=article_data['webUrl'],
#             headline=article_data['fields']['headline'],
#             trail_text=article_data['fields']['trailText'],
#             body=article_data['fields']['body'],
#             date=timezone.now(),
#             summary=summary,
#             question=question,
#         )
#         new_article.save()

#         return new_article
    
#     except Article.DoesNotExist:
#         print("Corresponding Guardian article not found.")
#         return None
    
#     except Exception as e:
#         print(f"An error occurred while saving generated question: {e}")
#         return None

# def save_generated_question(article_id, summary, question):
#     try:
#         Article.objects.filter(id=article_id).update(summary=summary, question=question, date=timezone.now())
#         return True
#     except Article.DoesNotExist:
#         print("Article not found.")
#         return False
#     except Exception as e:
#         print(f"An error occurred while saving generated question: {e}")
#         return False

def save_generated_question(article_id, summary, question):
    try:
        # Retrieve the Article object by its ID
        article = Article.objects.get(id=article_id)

        print(article_id)
        print(article)
        
        # Update the summary and question fields
        article.summary = summary
        article.question = question

        print(article.summary)
        print(article.question)
        
        # Save the changes to the database
        article.save()
        
        return True
    except Article.DoesNotExist:
        print("Article not found.")
        return False
    except Exception as e:
        print(f"An error occurred while saving generated question: {e}")
        return False
