import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.callbacks.streamlit import StreamlitCallbackHandler

load_dotenv()

llm = OpenAI(temperature=0.7, openai_api_key=os.getenv('OPENAI_API_KEY'))
tools = load_tools(['google-search'])
agent = initialize_agent(
    tools=tools, llm=llm
)

st.set_page_config(page_title='LangChain Agents - Generative Text AI', page_icon='🦜️')
st.title('LangChain Agents - HL')

if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'assistant', 'content': 'How can I help you?'}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if prompt := st.chat_input(placeholder='What day is it today?'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)

    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler()
        response = agent.run(st.session_state.messages)
        st.session_state.messages.append({'role': 'assistant', 'content': response})
        st.write(response)
