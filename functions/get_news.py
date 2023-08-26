import pandas as pd
import numpy as np


def make_clickable(link,text):
    # target _blank to open new window
    # extract clickable text to display for your link
    return f'<a target="_blank" href="{link}">{text}</a>'

def get_news(content,prediksi):
    link = ["https://stackoverflow.com/questions/71641666/hyperlink-in-streamlit-dataframe",
            "https://stackoverflow.com/questions/71731937/how-to-plot-comparison-in-streamlit-dynamically-with-multiselect"]
    text = ["Hyperlink in Streamlit dataframe",
            "How to plot comparison in Streamlit dynamically with multiselect?"]
    if prediksi == 'Hoax':
        prediksi = 'Kontradiksi'
    else:
        prediksi = 'Selaras'
    df = pd.DataFrame(
        {
            "Link Berita": [make_clickable(link[0],text[0]),
                    make_clickable(link[1],text[1])],
            "Isi": [prediksi, prediksi]
        }
    )
    return df
