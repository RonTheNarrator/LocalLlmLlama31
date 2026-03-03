import streamlit as st
import numpy as np

st.markdown("# Main page 🎈")

m = st.chat_message("Ai")
m.write("Sup")

if "test" not in st.session_state:
  st.session_state.test = np.random.random([3,3])

m.dataframe(st.session_state.test)

m.image("./streamLitApps/firstAppTraining/resources/someCode.png")

st.write("EndOfMessage")