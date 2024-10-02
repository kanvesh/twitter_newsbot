from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('openai_api_key')
client = OpenAI(api_key = openai_api_key)

def return_comment(headline):
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are a sarcastic and witty assistant good at puns"},
        {"role": "user", "content": "Provide a short, sharp, witty, caustic comment under 6 words on this news headline: "+headline}
      ]
    )
    return response.choices[0].message.content
