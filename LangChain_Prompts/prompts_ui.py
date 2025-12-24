from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
import os
from langchain_core.prompts import load_prompt

base_dir = os.path.dirname(__file__)
template_path = os.path.join(base_dir, "template.json")
template = load_prompt(template_path)

load_dotenv()
# model = ChatOpenAI()
model = ChatOpenAI(api_key="OPEN AI_API_KEY", temperature=0.7)


st.header('Reasearch Tool')
# user_input= st.text_input('Enter your query here')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')



if st.button('Summarize'):
    # result = model.invoke(user_input)
    st.write("Hello")
    # st.text('Some random text')
    # chain = template | model
    # result = chain.invoke({
    #     'paper_input':paper_input,
    #     'style_input':style_input,
    #     'length_input':length_input
    # })
    # st.write(result.content)