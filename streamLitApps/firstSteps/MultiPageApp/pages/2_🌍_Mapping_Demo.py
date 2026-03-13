import streamlit as st

hour_to_filter = st.slider("hour",0,23,17)
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(data[data[DATE_COLUMN].dt.hour == hour_to_filter])