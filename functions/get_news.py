import pandas as pd
import numpy as np
from googlesearch import search

def make_clickable(link,text):
    # target _blank to open new window
    # extract clickable text to display for your link
    return f'<a target="_blank" href="{link}">{text}</a>'

def get_news(content,prediksi):
 
    results = search(content,num_results=5,lang="id",advanced=True)
    results = list(results)
    link = [result.url for result in results]
    text = [result.title for result in results]
    
    if prediksi == 'Hoaks':
        prediksi = 'Kontradiksi'
    else:
        prediksi = 'Selaras'
    link_berita = [make_clickable(l,t) for l,t in zip(link,text)]
    isi = [prediksi for i in range(len(link_berita))]
    df = pd.DataFrame(
        {
            "Link Berita": link_berita,
            "Isi": isi,
        }
    )
    return df
