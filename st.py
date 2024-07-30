import streamlit as st
import spacy
import spacy_streamlit
import joblib
import numpy as np

@st.cache_resource
def load_spacy_model():
    return spacy.load("drop00")

@st.cache_resource
def load_rf_model():
    return joblib.load("classif.pkl")

nlp = load_spacy_model()
rf_model = load_rf_model()

st.title("Détection d'entités et Classification de texte")

model_choice = st.radio("Choisissez le modèle :", ["Détection d'entités nommées", "Classification"])

user_input = st.text_area("Entrez votre texte ici:")


if st.button("Launch"):
    if model_choice == "Détection d'entités nommées":
        doc = nlp(user_input)
        spacy_streamlit.visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
    elif model_choice == "Classification":
        text_features = [user_input]
        prediction = rf_model.predict(text_features)
        
        if prediction[0] == 1:
            st.write("Classification : Grève")
        else:
            st.write("Classification : Pas de grève")