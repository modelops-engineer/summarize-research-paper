from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()


# LLM does not have memory so we are appending the conversation in the list, so that it can 
# store them as it's memory and it will go to model as input
chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input.lower() == "exit":
        break
    
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI:", result.content)