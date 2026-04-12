import streamlit as st 
from langchain_ollama import ChatOllama
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage
from langchain_core.callbacks.base import BaseCallbackHandler



##Arxiv and wikipedia Tools
arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=500)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=500)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

search=DuckDuckGoSearchRun(name="Search")

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text
 
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.re(token)



st.title("🔎 Langchain - Chat with AI Search")

if "messages" not in st.session_state:
    st.session_state["messages"]={
        "messages":[AIMessage("Hi, I'm a chatbot who can search the web. How can I help?")]
    }

for msg in st.session_state.messages["messages"]:
    if type(msg) == HumanMessage:
       role = "user"
    elif type(msg) == AIMessage and len(msg.content)>0:
       role = "assistant"
    else:
       continue
    st.chat_message(role).write(msg.content)
    
    
if prompt:=st.chat_input(placeholder="What is machine learning?"):
  st.session_state.messages["messages"].append(HumanMessage(prompt))
  st.chat_message("user").write(prompt)

  llmOllama = ChatOllama(
    model="llama3.1:8b",
    temperature=0
  )
  tools=[arxiv,wiki,search]
  agent = create_agent(model=llmOllama, tools=tools, system_prompt="You are a helpful assistant")
  st_cb=StreamHandler(st.sidebar.container())

  with st.chat_message("assistant"):
    st.session_state.messages=agent.stream(st.session_state.messages, config = {"callbacks":[st_cb]})
    st.write(st.session_state.messages["messages"][-1].content)
    st.sidebar.write(st.session_state.messages)


#Can a barnacle reattach itself if its detached