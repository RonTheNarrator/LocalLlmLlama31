import streamlit as st 
from langchain_ollama import ChatOllama
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain.agents import create_agent


##Arxiv and wikipedia Tools
arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=500)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=500)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

search=DuckDuckGoSearchRun(name="Search")




st.title("🔎 Langchain - Chat with AI Search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more Langchain 🤝 Streamlit Agent examples at [https://github.com/langchain-ai/streamlit-agent]
""" 

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a chatbot who can search the web. How can I help?"}
    ]
    
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])
    
    
if prompt:=st.chat_input(placeholder="What is machine learning?"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)
    
    llmOllama = ChatOllama(
    model="llama3.1:8b",
    temperature=0
    )
    tools=[arxiv,wiki,search]
    agent = create_agent(model=llmOllama, tools=tools, system_prompt="You are a helpful assistant")
    st_cb=StreamlitCallbackHandler(st.sidebar.container(), expand_new_thoughts=False)

    with st.chat_message("assistant"):
        response=agent.invoke({"messages": st.session_state.messages}, callbacks=[st_cb])
        st.write(response)
        st.session_state.messages.append({'role':'assistant',"content":response["messages"][-1].content})