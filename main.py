import streamlit as st
from streamlit_chat import message

from embedchain import App

chatbot = App()
chatbot.add_local("pdf_file", "pdf/book_comportamental.pdf")

if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello ! Ask me anything 🤗"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Hey ! 👋"]
    

response_container = st.container() # container for the chat history
container = st.container() # container for the user's text input

with container:
    with st.form(key='my_form', clear_on_submit=True):
        
        user_input = st.text_input("Query:", placeholder="What you want to know?", key='input')
        submit_button = st.form_submit_button(label='Send')
        
    if submit_button and user_input:
        output = chatbot.chat(user_input)
        
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
            message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")