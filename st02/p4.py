import streamlit as st
from PIL import Image
import pandas as pd

#Side Bar
st.sidebar.markdown("Clicked Page4")


#Page
st.title("Page 4")

st.audio("data/tts_audio.mp3")

image = Image.open("img/ing.jpg")
st.image(image, caption="예제이미지", use_container_width=True)

#st.audio("example.mp3")

#st.video("example.mp4")

df = pd.read_csv('data/booksv_02.csv') #booksv_02.csv 파일이 위치한 경로 지정
st.write(df)
st.dataframe(df)
#st.table(df)
st.json({
    '이름': '이시현',
    '나이': 24,
    '거주지': '광주'
})
st.metric(label="LG전자", value="78,000원", delta="2.12%")
st.metric(label="현대차", value="150,000원", delta="-1.25%")