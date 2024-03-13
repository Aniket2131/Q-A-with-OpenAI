import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api = st.sidebar.text_input('Please Provide Your OpenAI API', type='password')


def get_response(input_text):
    llm = OpenAI(temperature=1, openai_api_key=openai_api)
    res = llm(input_text)
    st.info(res)


with st.form('my_form'):
    text = st.text_area('Enter text', 'Ask your Question')
    submit = st.form_submit_button('Submit')

    if submit and not openai_api.startswith('sk-'):
        st.warning('Invalid API', icon='⚠')

    if submit and openai_api.startswith('sk-'):
        get_response(text)


