# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()

# content ="사과"

# chat_response = chat_model.invoke(content + "에 대한 시를 써줘")
# print(chat_response.content)

import streamlit as st

st.title("인공지능 시인")

content = st.text_input("시의 주제를 입력해주세요. ")

# if st.button("시 작성해줘!"):
if st.button("시 작성해줘!", type="primary", icon="🔥"):
    with st.spinner("Wait for it...", show_time=True):
    # with st.spinner(content + " 시 작성중...."):
      chat_response = chat_model.invoke(content + "에 대한 시를 써줘")
      st.write(chat_response.content)
