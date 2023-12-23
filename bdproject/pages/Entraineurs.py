import streamlit as st
import pandas as pd
import requests
import time
from datetime import date

st.markdown("# LES ENTRAINEURS DISPONIBLES 🏅")
st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
st.sidebar.markdown("# Gestion des entraineurs 🏅")
st.write("*Nos entraîneurs dévoués sont là pour vous guider, vous soutenir et vous aider à atteindre vos objectifs, tout en créant un environnement où vous vous sentez à l'aise et confiant.*")
st.image('pages/photo/FIND YOUR COACH.png', caption="FIND YOUR PERSONAL COACH ")
st.write("*****Voici les entraîneurs disponibles pour le moment:*****")

def fetch_data(columns=None):
    try:
        url = 'https://apex.oracle.com/pls/apex/bd24_tp2/entraineur1/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        data = response.json()["items"]

        if columns:
            data = [{col: item.get(col) for col in columns} for item in data]
        return data
    
    except requests.exceptions.RequestException as e:
        st.error(f'Error during HTTP request: {e}')
        return None

columns_to_fetch = ['nom', 'prenom', 'datenaissance', 'email', 'numerotelephone']
data = fetch_data(columns_to_fetch)

if data is not None:
    for item in data:
        st.markdown(f"**Nom:** {item['nom']}  \n**Prénom:** {item['prenom']}  \n**Date de Naissance:** {item['datenaissance']}  \n**Email:** {item['email']}  \n**Numéro de Téléphone:** {item['numerotelephone']}  \n")
        st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

else:
    st.error("Failed to fetch data.")

def filter_data(data, last_name, date_range):
    filtered_data = []
    for item in data:
        if last_name.lower() in item.get('nom', '').lower():
            birth_date = pd.to_datetime(item.get('datenaissance'), errors='coerce').date()
            if date_range[0] <= birth_date <= date_range[1]:
                filtered_data.append(item)
    return filtered_data

data = fetch_data()
st.markdown("### Vous pouver chercher sur le nom du coach et son age qui vous plaise et devoiler vos meuilleures versions🥇🗓️")
st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

if data is not None:
    st.markdown("#### Chercher votre coach personnel")

    last_name_input = st.text_input("Chercher le nom de famille de votre coach:")
    
 
    date_range_input = st.date_input("Chercher par plage de dates de naissances:", [date(1900, 1, 1), date.today()])

    filtered_data = filter_data(data, last_name_input, date_range_input)
    if st.button("Chercher votre coach"):
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.006)
            progress_bar.progress(i)
        if not filtered_data:
            st.warning("Aucun entraîneur ne correspond aux critères de recherche.")
        else:
            st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
            st.markdown("***Les Entraîneurs disponibles selon votre choix:***")
            for item in filtered_data:
                st.markdown(f"**Nom:** {item['nom']}  \n**Prénom:** {item['prenom']}  \n**Date de Naissance:** {item['datenaissance']}  \n**Email:** {item['email']}  \n**Numéro de Téléphone:** {item['numerotelephone']}  \n")
                st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

            # Afficher la table d'entraîneurs disponibles comme la dernière
            st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
