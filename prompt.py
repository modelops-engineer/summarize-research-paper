from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st


load_dotenv()

model = ChatOpenAI()

st.header('Research Paper Summarizer')

paper_name = st.text_input('Enter the paper name...')

style_input = st.selectbox('Select the style...',[
    'Beginner-friendly',
    'Technical',
    'Code Oriented',
    'Detailed Explanation'
])

length_input = st.selectbox('Select the length of summary...',[
    'Short (1-2 Paragraph)',
    'Medium (3-5 Paragraphs)',
    'Long (Detailed explanation)'
])

template = load_prompt("template.json")

# place holders
prompt = template.invoke({
    'paper_name':paper_name,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)   
    st.write(result.content)