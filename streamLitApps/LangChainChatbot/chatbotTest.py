import streamlit as st
from langchain_ollama import ChatOllama

llm = ChatOllama(
  model="llama3.1:8b",
  temperature=0
)


def clearMessages():
    st.session_state["messages"] = []

if "messages" not in  st.session_state:
  clearMessages()


for m in st.session_state["messages"]:
  m.print()

def userSubmitMessage():
  x = st.session_state["userInputChatbox"]
  st.session_state["messages"].append(chatMessage(x))
  messages = [m.toAiMessage() for m in st.session_state["messages"]]
  st.session_state["messages"].append(chatMessage(llm.stream(messages),sender="ai"))
  
  #st.write_stream(llm.stream(x))

st.chat_input(
  key="userInputChatbox",
  on_submit=userSubmitMessage)


st.button("Clear", on_click=clearMessages)

class chatMessage:
  def __init__(self, content, sender="user"):
    self.sender = sender
    self.content = content

  def print(self):
    with st.chat_message(self.sender):
      if type(self.content) == str:
        st.write(self.content)
      else:
        self.content = st.write_stream(self.content)

  def toAiMessage(self):
    if self.sender== "user":
      role ="user"
    else:
      role ="assistant"
    return {"role": role, "content": self.content}
