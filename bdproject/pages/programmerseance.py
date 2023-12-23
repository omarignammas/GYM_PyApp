import streamlit as st
import requests
import time

st.markdown("# PROGRAMMER VOTRE SEANCE 🏁")
st.sidebar.markdown("# Gestion des séances 🏁")
st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
st.image("pages/photo/AJOUTER SEANCE.png", caption="ADD YOUR PERSONAL SESSION")


def fetch_data():
    try:
        url = 'https://apex.oracle.com/pls/apex/bd24_tp2/horaire1/?limit=10000'
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
def is_session_conflict(existing_data, new_codee, new_ids, new_jour, new_heure,new_gymsalle):
    for item in existing_data:
        if (
            item.get('codee') == new_codee
            and item.get('ids') == new_ids
            and item.get('gymsalle') == new_gymsalle
            and item.get('jour') == new_jour
            and item.get('heuredebut') == new_heure
        ):
            return True
    return False

def insert_record():
    st.header("programmer une nouvelle séance:")
    st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
    
    # Existing data
    data = fetch_data()

    CodeE = st.selectbox("**choisir Le Code de votre entraineur**", options=(item.get('codee') for item in data))
    st.write(CodeE)
    id_seance = st.selectbox("**choisir Id de votre séance**", options=(item.get('ids') for item in data))
    st.write(id_seance)
    gymsalle_seance = st.text_input("**Enter le nom de votre GymSalle**")
    jour_seance = st.selectbox("**Choisir le jour de votre séance**", options=(['lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']))
    st.write(jour_seance)
    heure_seance = st.selectbox("**choisir l'heure de debut de votre séance**", options=(["7:00", "8:00", "09:00", "11:00", "16:00", "16:30", "18:00", "19:30"]))
    st.write(heure_seance)
    duree_seance = st.selectbox("**choisir la duree(en minutes) de votre séance**", options=([30, 40, 45, 60]))
    st.write(duree_seance)

    if st.button("Ajouter Seance"):
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.006)
            progress_bar.progress(i)
        if is_session_conflict(data, CodeE, id_seance, jour_seance, heure_seance,gymsalle_seance):
            st.error('Un séance est déjà programmée dans cet horaire pour cet entraîneur,et merci.')
        else:
            url = 'https://apex.oracle.com/pls/apex/bd24_tp2/horaire1/'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'Content-Type': 'application/json',
            }
            data_request = {
                "codee": CodeE,
                "ids": id_seance,
                "gymsalle": gymsalle_seance,
                "jour": jour_seance,
                "heuredebut": heure_seance,
                "duree": duree_seance,
            }
            response = requests.post(url, headers=headers, json=data_request)

            if response.status_code == 201:
                st.success('Votre séance est programmée avec succès')
            else:
                st.error('Échec de la programmation de votre séance', response.text)


data = fetch_data() 

if data is not None:
    st.title("Les horaires disponibles :")
    st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

    st.write("*Voici les seances disponibles pour le moment*")
    table_data = [['CodeE','IdS','GYMSALLE', 'JOUR', 'HEURE DE DEBUT','DUREE DE SEANCE']] + [[item.get('codee'),item.get('ids'),item.get('gymsalle'), item.get('jour'), item.get('heuredebut'),item.get('duree')] for item in data]
    st.table(table_data)

    insert_record()
    
    # Filter and display the table
    col1, col2 = st.columns(2)
   
else:
    st.error("Failed to extract table nom from URL.")    