import os
from openai import OpenAI
from dotenv import load_dotenv

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

def generate_questions(article_data):
    formatted_prompt = (
        "You are a sociologist working to improve public policy. You are interested in the public opinion on current newsworthy topics.\n\n"
        "Write a one line summary of the provided article (do not prefix i.e. remove 'summary'), then write a yes/no question (do not prefix i.e. remove 'question') that, once presented to the general population, will result in insightful demographic data.\n\n"
        "News article below:\n\n"
        f"Headline: {article_data['headline']}\n"
        f"Trail Text: {article_data['trailText']}\n"
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
        # Extract and return the generated question
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred while generating the question: {e}")
        return "I couldn't generate a question."
    