import streamlit as st
import pandas as pd
import requests

st.markdown(
    """
    <style>
        body {
            background-color: #9FA0C3;  /* Remplacez cette couleur par celle que vous préférez */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("# LES SEANCES DISPONIBLES ❄️")
st.sidebar.markdown("# Gestion des séances ❄️")
# Add an image
st.image("pages/photo/CHOOSE SESSION.png", caption="CHOOSE YOUR PERFECT SESSION ")

def fetch_data():
    try:
        url = f'https://apex.oracle.com/pls/apex/bd24_tp2/seance1/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        data = response.json()["items"]
        return data
    except requests.exceptions.RequestException as e:
        st.error(f'Error during HTTP request: {e}')
        return None

data = fetch_data()

if data is not None:
    st.write("Calendrier des Séances:")
    data = fetch_data() 

if data is not None:
    st.title("Les seances disponibles :")

    # Display the table in Streamlit
    table_data = [['nom', 'type1', 'niveau']] + [[item.get('nom'), item.get('type1'), item.get('niveau')] for item in data]    
    col1, col2 = st.columns(2)   
    df = pd.DataFrame(table_data)
    st.table(df)

    st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
    st.write("Veuillez personnaliser votre choix.")

    select1 = st.selectbox("Veuillez choisir le niveau de la  seance ", options=(item.get('niveau')for item in data))
    st.write(select1)

    select2 = st.selectbox("Veuillez choisir le type de la séance", options=(item.get('type1')for item in data))
    st.write(select2)

    # Filtrer le DataFrame en fonction des sélections
    filtered_df = [['type1', 'niveau']] + [[select1 , select2] ]   
    col1, col2 = st.columns(2)   
    df = pd.DataFrame(filtered_df)
    #filtered_df = df[( (df['type1'] == select1) & df['niveau'] == select2)]
    
    # Afficher les séances filtrées
    st.table(filtered_df)
