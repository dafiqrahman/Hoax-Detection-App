import streamlit as st
import pandas as pd
import numpy as np
from functions.deteksi import deteksi
from functions.get_news import get_news
#streamlit makes 2 columns
# st.set_page_config(layout="wide")


st.title('Hoax Detection App')
st.write('Aplikasi ini digunakan untuk mendeteksi berita hoax berdasarkan isi berita. Model yang digunakan adalah DistilBERT. Dataset yang digunakan adalah Dataset Berita Palsu dan Nyata dari Kaggle dan Jurnal terkait.')
st.header('Input Berita')
col1, col2 = st.columns(2)

API_KEY = "st.secrets["API_TOKEN"]
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
        hoax, valid, prediksi = deteksi(konten,API_KEY)
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
        



