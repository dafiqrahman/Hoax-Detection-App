import streamlit as st
import pandas as pd
import numpy as np
from functions.deteksi import deteksi
from functions.get_news import get_news
#streamlit makes 2 columns
# st.set_page_config(layout="wide")

st.title('Hoax Detection App')
st.write('This app is used to detect hoax news based on the title and the content of the news. The model used is a combination of LSTM and CNN. The dataset used is the Fake and Real News Dataset from Kaggle.')
st.header('Input Content')
col1, col2 = st.columns(2)

#input
with col1:
    konten = st.text_area('Masukkan isi konten yang ingin dideteksi')
#button
deteksi_button = st.button('Deteksi')
#output
with col2:
    st.write("  ")
    sub_col1, sub_col2,sub_col3 = st.columns(3)
    if deteksi_button:
        hoax, valid, prediksi = deteksi(konten)
        sub_col1.metric(label='Hoax', value=hoax)
        sub_col2.metric(label='Valid', value=valid)
        sub_col3.metric(label='Prediksi', value=prediksi)
    else:
        sub_col1.metric(label='Hoax', value='???')
        sub_col2.metric(label='Valid', value='???')
        sub_col3.metric(label='Prediksi', value='???')
st.write("---")
if deteksi_button:
    st.subheader("Berita yang mirip dengan konten yang dimasukkan")
    df = get_news(konten,prediksi)
    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
        



