from google import genai

client = genai.Client(
    api_key="AIzaSyD_4csyqV3Zhxx7tc9wGHEifXoopdRN4-I"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a 5 lines"
)

print(response.text)