import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a comedian named Alex, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a comedic script that explains the concept of being human."}
  ]
)

print(completion.choices[0].message.content)