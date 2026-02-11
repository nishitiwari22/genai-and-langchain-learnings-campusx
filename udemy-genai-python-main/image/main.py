from dotenv import load_dotenv
import os
from openai import OpenAI

# Load .env file
load_dotenv()

# ✅ Fetch from environment variable, not hardcode
api_key = os.getenv("OPENAI_API_KEY")
print("API Key Loaded?", bool(api_key))  # Debug line

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Generate a caption for this image in about 50 words"},
                {"type": "image_url", "image_url": {"url": "https://images.pexels.com/photos/879109/pexels-photo-879109.jpeg"}}
            ]
        }
    ]
)

print("Response:", response.choices[0].message.content)
