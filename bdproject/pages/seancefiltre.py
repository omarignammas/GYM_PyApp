import streamlit as st
import requests
import time

# Ajouter du HTML pour personnaliser le style
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
st.markdown("# CHOISIRE VOTRE SEANCE🏋🏼")
st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
st.sidebar.markdown("# Gestion des séances 🏋🏼")
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
        st.error(f'Erreur lors de la requête HTTP : {e}')
        return None

data = fetch_data()

if data is not None:
    st.write("Voici toutes les séances disponiles maintenant :")

    # Créer une liste pour stocker les données des éléments
    table_data = []

    # Ajouter les en-têtes du tableau
    table_data.append(['NOM', 'TYPE', 'NIVEAU'])

    # Ajouter les données de chaque élément à la liste
    for item in data:
        table_data.append([item.get('nom'), item.get('type1'), item.get('niveau')])

    # Afficher le tableau dans Streamlit
    st.table(table_data)

    # Créer 2 colonnes
    col1, col2 = st.columns(2)

    # Sélecteur pour filtrer par niveau
    with col1:
        st.markdown("Choisir Votre Niveau S'il Vous Plait:")
        selected_niveau = st.multiselect("Niveau", [1, 2, 3, 4])

    # Sélecteur dynamique pour filtrer par typ
    with col2:
        st.markdown("Choisir Votre Type S'il Vous Plait:")
        unique_typ_values = set(row[1] for row in table_data[1:])  # Get unique "typ" values
        selected_typ_values = st.multiselect("Type", list(unique_typ_values))

    # Filtrer les données en fonction des sélections
    filtered_data = [table_data[0]]  # Ajouter les en-têtes au tableau filtré

    for row in table_data[1:]:
        niveau = row[2]
        typ = row[1]

        niveau_condition = niveau in selected_niveau
        typ_condition = typ in selected_typ_values

        if niveau_condition or typ_condition:
            filtered_data.append(row)

    # Afficher le tableau filtré dans Streamlit
    if st.button("Trouver votre Seance"):
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.006)
            progress_bar.progress(i)
    st.markdown("Voici les seances disponibles en fonction des niveaux et types sélectionnés:")
    st.table(filtered_data)
else:
    st.error("Impossible d'extraire le nom de la table à partir de l'URL.")
