import streamlit as st

#Sidebar
st.sidebar.markdown("Clicked Page1")
st.sidebar.markdown("Side Menu")
st.sidebar.button("Click")
st.sidebar.radio("성별", ["여자", "남자"])

#Title
st.title("Page 1")
st.markdown("Mark Down")
st.header("Header")
st.subheader("Sub Header")
st.caption("Caption")
st.code("""
    def func():
        print("OK")
    def func2():
        print("OOOOOOOOOOO")
 """, language="python")