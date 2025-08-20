import streamlit as st

page_main = st.Page("main.py", title="Main Page",  icon="🎈")
page_1 = st.Page("p1.py", title="Page 1", icon="🎉")
page_2 = st.Page("p2.py", title="Page 2", icon="🎉")
page_3 = st.Page("p3.py", title="Page 3", icon="🎉")
page_4 = st.Page("p4.py", title="Page 4", icon="🎉")
page_5 = st.Page("p5.py", title="Page 5", icon="🎉")
#클릭을 할 때 마다 page 1,2,3이 나옴

#st.click(icon)

page = st.navigation([page_main, page_1, page_2, page_3, page_4, page_5]) #리스트 형태로

page.run()