import streamlit as st

#Side Bar
st.sidebar.markdown("Clicked Page7")


#Page
st.title("Page 7")


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)