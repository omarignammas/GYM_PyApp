import streamlit as st
import requests
import pandas as pd

st.markdown("# GRAPHES SEANCES 📈📊")
st.sidebar.markdown("# Gestion des séances 🏁")
st.markdown('<hr style="border:3px solid #0077cc;">', unsafe_allow_html=True)
st.image("pages/photo/GRAPHICS.png", caption="GRAPHICS SESSIONS")


def fetch_data(columns=None):
    url = 'https://apex.oracle.com/pls/apex/bd24_tp2/horaire1/?limit=10000'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()['items']

        if columns:
            data = [{col: item.get(col) for col in columns} for item in data]
        return data
        
    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')

columns_to_fetch = ['ids','jour','heuredebut']  
data = fetch_data(columns_to_fetch)

df = pd.DataFrame(data)

st.table(df)
st.title("Graphique à barres")
st.markdown('**Nombre de séances par plage horaire** 📊')
bar_chart_data = df.groupby('heuredebut').size()
st.bar_chart(bar_chart_data)

st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

st.title("Graphique à lignes")
st.markdown('***Nombre de séances par jour de la semaine*** 📈 ')
line_chart_data = df.groupby('jour').size().sort_values(ascending=False)
st.line_chart(line_chart_data)
