from openai import OpenAI
import re
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('openai_api_key')
client = OpenAI(api_key = openai_api_key)



def get_first_numeric(string):
    # Use a regular expression to find the first numeric in the string
    match = re.search(r'\d+', string)
    if match:
        return int(match.group())  # Return the first numeric found
    else:
        return 0  # Return None if no numeric is found



def get_joke_potential_score(headline):
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are a humorous evaluator"},
        {"role": "user", "content": "Provide a score of 1-10 on how much potential for humor is present in this headline. Just return the number:"+ headline}
      ],
        temperature=0.7,
        max_tokens=60
    )
    # Extracting the rating and explanation from GPT-4
    evaluation = response.choices[0].message.content.strip()
    return get_first_numeric(evaluation)
