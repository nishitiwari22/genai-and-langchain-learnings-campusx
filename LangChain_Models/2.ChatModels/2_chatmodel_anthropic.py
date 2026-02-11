from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke('What is the capital of India')

print(result.content)

# I have written and tried to  debug the code and it works fine. Since the Claude API is paid hence I am unable to share the output here.