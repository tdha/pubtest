import openai
import os
from dotenv import load_dotenv

load_dotenv("pubtest/.env")

def ask_chatgpt(question):
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("No OpenAI API key found. Check your .env file.")
        return "No API key provided."
    
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't fetch a response. Please try again later."
