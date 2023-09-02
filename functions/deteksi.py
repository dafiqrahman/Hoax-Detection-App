import numpy as np
import requests

def deteksi(content,API_TOKEN):
    #dummy detection based on random
    #random float between 0 and 1


    API_URL = "https://api-inference.huggingface.co/models/dafqi/DistilBERT-Hoax-Detection"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": content,
        "wait_for_model": True,
    })
    prediksi = output[0][0]['label']
    if prediksi == 'Hoaks':
        hoax = output[0][0]['score']
        valid = 1 - hoax
    else:
        valid = output[0][0]['score']
        hoax = 1 - valid
    hoax = round(hoax,2)
    valid = round(valid,2)
    return hoax, valid, prediksi
