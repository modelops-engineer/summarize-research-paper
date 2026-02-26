from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content='You are an expert of AI development'),
    HumanMessage(content='Tell me about Langchain and RAG')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))