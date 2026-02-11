# Persona Based Prompting
import os
from dotenv import load_dotenv   # ✅ correct import
from openai import OpenAI        # ✅ correct import

import json
# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client using API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Piyush Garg.
    You are acting on behalf of Nishi Tiwari who is 23 years old Tech enthusiast and 
    principal engineer. Your main tech stack is JS and Python and you are learning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, What's up!

    (100 - 150 examples)
"""

# Create a chat completion
response = client.chat.completions.create(
    model="gpt-4o-mini",   # ✅ use gpt-4o-mini for faster response
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "who are you?"}
    ]
)

print("Response:", response.choices[0].message.content)
