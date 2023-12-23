import streamlit as st
import requests
import pandas as pd
import json

st.markdown("# GRAPHES SEANCES 📈📊")
st.sidebar.markdown("# Gestion des séances 🏁")

def fetch_data(columns=None):
    url = 'https://apex.oracle.com/pls/apex/bd24_tp2/horaire1/?limit=10000'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
        data = response.json()['items']

        if columns :
            data = [{col:item.get(col) for col in columns} for item in data]
        return data
         
        
    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')
st.markdown("**les horaires disponibles**")
columms_to_fetch = ['jour','heuredebut']
data = fetch_data(columms_to_fetch)
st.table(data)
#graphe de batton
df = pd.DataFrame(data)
st.title('Graphique à barre 📊')
st.bar_chart(df.set_index('heuredebut'))
#graphe lineaire
df = pd.DataFrame(data)
st.title('Graphique à ligne 📈')
st.line_chart(df.set_index('heuredebut'))