import streamlit as st

page_main = st.Page("main.py", title="Main Page")
page_1 = st.Page("p1.py", title="Page 1")
page_2 = st.Page("p2.py", title="Page 2")
page_3 = st.Page("p3.py", title="Page 3")
#클릭을 할 때 마다 page 1,2,3이 나옴

page = st.navigation([page_main, page_1, page_2, page_3]) #리스트 형태로

page.run()