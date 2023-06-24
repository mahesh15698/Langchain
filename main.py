# intergrate our code OpenAI API
import os 
from constant import openai_key
from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# Streamlet framework
st.title('Langchain Demo woth OpenAI API')
input_text = st.text_input("Search the topic u want")

#OpenAI
llm = OpenAI(temperature=0.8,)

if input_text:
    st.write(llm(input_text))
