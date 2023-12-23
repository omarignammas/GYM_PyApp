import streamlit as st

def main():
   st.title("WELCOME TO IGNITE GYM's APPLICATION 🏋🏼🥋🚴🏽‍♀️🏊🏽‍♀️")
   st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

   st.markdown("##### Chez IGNITE GYM, nous vous promettons bien plus qu'on est un groupe des salles de sport le premier partout au maroc. Nous sommes une communauté passionnée dédiée à l'amélioration de votre bien-être physique et mental pour la socitee marocaine . Avec une gamme d'activités allant de la musculation revitalisante au cardio stimulant, du boking énergique au karaté dynamique et au teakwondo, nous offrons une expérience de remise en forme complète et diversifiée. Chez IGNITE GYM, nous croyons en l'autonomie de nos membres. Nous vous invitons à choisir vos propres séances en fonction de vos préférences et de votre niveau de confort. Nos entraîneurs dévoués sont là pour vous guider, vous soutenir et vous aider à atteindre vos objectifs, tout en créant un environnement où vous vous sentez à l'aise et confiant. Rejoignez-nous chez IGNITE GYM, où l'ignition de votre passion pour la santé et la forme physique commence, et ensemble, nous atteindrons de nouveaux sommets")
   st.sidebar.markdown("# Menu ❄️")


   st.image("pages/photo/IGNITE GYM.png", caption="Ignite Fitness Gym invite you around the world")


   st.markdown("### IGNITE GYM's VOUS DONNE LA POSSIBILITE DE TROUVER VOTRE SEANCE PERSONNEL COMPATIBLE AVEC VOTRE NIVEAU ,ET AVEC UN COACH DE VOTRE CHOIX ET DANS LA SALLE QUI VOUS PLAISE 🥇🥈🥉 ")

   st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

   st.markdown("#### Bienvenue dans notre application dédiée à la gestion de votre expérience sportive à IGNITE GYM! Voici un aperçu des fonctionnalités qui rendront votre expérience encore plus enrichissante :")
   dernier_texte = """
1. **Page d'Accueil Personnalisée :**
   - Présentation du projet, de ses objectifs et des personnes derrière sa réalisation.
  
2. **Explorer les Séances :**
   - Découvrez et filtrez les séances disponibles en fonction de vos préférences.
   - Obtenez des métriques clés comme le nombre total de séances et les types distincts.
   - Affichez les horaires détaillés des séances qui vous intéressent.

3. **Découvrir les Entraineurs :**
   - Explorez les entraineurs disponibles avec la possibilité de filtrer par nom et date de naissance.
  
4. **Visualiser avec des Graphiques :**
   - Accédez à des graphiques intuitifs illustrant le nombre de séances par plage horaire et par jour de la semaine.

5. **Inscription de Nouvelles Séances :**
   - Utilisez un formulaire convivial pour insérer de nouvelles séances avec des vérifications intégrées.
   - Assurez-vous que chaque champ est correctement rempli, avec des contrôles pour la durée maximale et la disponibilité des créneaux.

6. **Inscription de Séances Hebdomadaires :**
   - Programmez de nouvelles séances hebdomadaires avec un formulaire interactif.
   - Choisissez votre entraineur et la séance parmi des menus déroulants intuitifs.
   - Profitez de contrôles automatisés pour éviter les conflits d'horaires.

Notre application vous offre une immersion complète dans le monde dynamique de IGNITE GYM. Profitez de la personnalisation, des filtres intuitifs et des fonctionnalités de gestion pour tirer le meilleur parti de votre parcours sportif. Rejoignez-nous dans cette aventure et programmez votre réussite! 🏋️‍♂️💪🔥
"""

# Affichez le dernier texte sur Streamlit
   st.markdown(dernier_texte, unsafe_allow_html=True)
   st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)

   st.markdown("*Ce projet est developper par: Omar IGNAMMAS ET Najib HABLOUZ //C.INFO1* 🎖️")
   st.markdown('<hr style="border:2px solid #0077cc;">', unsafe_allow_html=True)
   st.markdown('**Contact us:@IGNITE GYM**')



if __name__=="__main__":
   main()