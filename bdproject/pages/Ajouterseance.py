import streamlit as st
import requests
import time


st.markdown("# AJOUTER SEANCE  🏁")
st.sidebar.markdown("# Gestion des séances 🏁")
st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
st.write("*Chez IGNITE GYM, nous croyons en l'autonomie de nos membres. Nous vous invitons à choisir vos propres séances en fonction de vos préférences et de votre niveau de confort.*")
st.image("pages/photo/ADD SESSION.png", caption="ADD YOUR PERSONAL SESSION ")

def fetch_data():
    try:
        url = f'https://apex.oracle.com/pls/apex/bd24_tp2/seance1/?limit=10000'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        data = response.json()["items"]
        return data
    except requests.exceptions.RequestException as e:
        st.error(f'Error during HTTP request: {e}')
        return None
    
def is_session_conflict(table_data,nom_session,type_session,niveau_session):
    for item in table_data:
        if (
            item.get('nom') == nom_session
            and item.get('type1') == type_session
            and item.get('niveau') == niveau_session
        ):
            return True
    return False

def insert_record():
    
    st.header("Ajouter une nouveau seance:")
    nom_input = st.text_input("Enter le nom de la seance:")
    type1_input = st.selectbox("Type de séance:", ["karate", "Teakwando", "Musculation","Natation","Cardio","Boxing"])
    niveau_input = st.selectbox("Niveau:", [1, 2, 3, 4])
    data=fetch_data()
    if st.button("Ajouter Seance"):
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.006)
            progress_bar.progress(i)
        if(is_session_conflict(data,nom_input,type1_input,niveau_input)):
             st.error("cette seance est deja ajoutee !")
        else:
         url = f'https://apex.oracle.com/pls/apex/bd24_tp2/seance1/'
         headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Content-Type': 'application/json',
         }
         data = {
            "nom": nom_input,
            "type1": type1_input,
            "niveau": niveau_input,
         }
         response = requests.post(url, headers=headers,json=data)

        if response.status_code == 201:
            st.success('Votre seance est inserer avec succees')
        else:
            st.error('Echoue dinsertion de votre seance : ', response.text)

data = fetch_data() 

if data is not None:
    st.title("Les seances disponibles :")
    st.write("Voici les seances disponibles pour le moment")
    table_data = [['NOM', 'TYPE', 'NIVEAU']] + [[item.get('nom'), item.get('type1'), item.get('niveau')] for item in data]
    st.table(table_data)
    st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

    insert_record()

    col1, col2 = st.columns(2)
   

else:
    st.error("Failed to extract table nom from URL.")    