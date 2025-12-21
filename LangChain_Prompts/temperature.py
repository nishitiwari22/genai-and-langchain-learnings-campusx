from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_temperature_model(temperature: float = 0.7):
	model = ChatOpenAI(temperature=temperature)
	result = model.invoke("Write a 5 line poem about the sea.")
	print(result)