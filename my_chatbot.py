from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# Giving context to chatbot for user input and AI output of the conversation

chat_history = [
    SystemMessage(content = "You are an expert of AI development")
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content = user_input))
    if user_input.lower() == "exit":
        break
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI:", result.content)