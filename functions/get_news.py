import pandas as pd
import numpy as np
import requests

def make_clickable(link,text):
    # target _blank to open new window
    # extract clickable text to display for your link
    return f'<a target="_blank" href="{link}">{text}</a>'

def get_news(content,prediksi,API_SEARCH_TOKEN,CSE_TOKEN):
 #import library request
    QUERY = "Video “Inul Daratista berbagi hadiah melalui akun Facebook 𝗜𝗻𝘂𝗹 𝗗𝗮𝗿𝗮𝘁𝗶𝘀𝘁𝗮 𝗦𝘂𝗿𝗽𝗿𝗮𝗶𝘀”"
    results = requests.get(f"https://www.googleapis.com/customsearch/v1?key={API_SEARCH_TOKEN}&cx={CSE_TOKEN}&q={QUERY}").json()['items']
    title = [result['title'] for result in results]
    link = [result['link'] for result in results]
    
    if prediksi == 'Hoaks':
        prediksi = 'Kontradiksi'
    else:
        prediksi = 'Selaras'
    link_news = [make_clickable(l,t) for l,t in zip(link,title)]
    title = [prediksi for i in range(len(link_news))]
    df = pd.DataFrame(
        {
            "Link Berita": link_news,
            "Isi": title,
        }
    )
    return df
