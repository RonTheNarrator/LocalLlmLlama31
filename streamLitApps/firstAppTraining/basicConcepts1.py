import streamlit as st
import pandas as pd
import numpy as np
import time


if "run_counter" not in st.session_state:
  st.session_state.run_counter = 0

st.session_state.run_counter += 1

st.write(f"This is your {st.session_state.run_counter} run of this page")

st.text_input("Your_name",key="name")

df = pd.DataFrame({
  'first':[1,2,3],
  'second':[4,5,6],
  'third':[4,5,6]
})

#df




dataframe = pd.DataFrame(
  np.random.randn(10,20),
  columns=('col %d' % i for i in range(20))
)
#st.dataframe(dataframe.style.highlight_max(axis=0,color="gray"))
#st.table(dataframe)

chart_data = pd.DataFrame(
  np.random.randn(20,3),
  columns=['a','b','c']
)

#st.line_chart(chart_data)
if st.checkbox("Show Map"):
  map_data = pd.DataFrame(
    np.random.rand(1000,2)/[50,51] + [50.30, 19.15],
    columns=['lat','lon']
  )
  st.map(map_data)

x = st.slider('x')
st.write(x,"squared is",x*x)
st.session_state.name

option = st.selectbox("pick:", df['second'])

option

phone_number = st.sidebar.slider("input your phone:",100000000,999999999)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column,right_column = st.columns(2)

left_column.button("X")
with right_column:
  st.expander("xd").dataframe(df)


bar = st.progress(0)
for i in range(20):
  bar.progress((i+1)*5)
  time.sleep(0.1)
"Done"