import streamlit as st

main_page = st.Page("multipageMain.py", title="Main Page", icon="🎈")
basicConcepts = st.Page("basicConcepts1.py")

pg = st.navigation([main_page, basicConcepts])

pg.run()