import streamlit as st

def calculate_sum(n1, n2):
    return n1 + n2



#Side Bar
st.sidebar.markdown("Clicked Page6")


#Page
st.title("Page 6")

n1 = st.number_input("First Number")
n2 = st.number_input("Second Number")

if st.button("Calculate"):
    st.write("Summation is: " + str(calculate_sum(n1, n2)))