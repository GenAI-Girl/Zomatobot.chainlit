import os
from openai import OpenAI
from src.prompt import system_instruction
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": system_instruction}
]


def ask_order(messages, model="gpt-3.5-turbo",temperature=0):
    response = client.chat.completions.create(
        model= model,
        messages=  messages,
        temperature= temperature 
    )

    return response.choices[0].message.content