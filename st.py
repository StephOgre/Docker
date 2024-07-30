import streamlit as st
import spacy

import spacy_streamlit

models = ["drop00"]
default_text = """
AIR FRANCE-KLM, plus forte baisse du SRD à la mi-séance du mardi 23 avril 2019 AIR FRANCE-KLM (-4,86% à 10,58 euros) Le syndicat national des pilotes de ligne (SNPL) aurait envoyé un préavis de grève au gouvernement pour exiger le maintien de la représentativité spécifique des pilotes et de la caisse de retraite du personnel navigant. C'est ce qu'a révélé jeudi soir la Tribune. Le mouvement débuterait le lundi 6 mai et s'achèverait le samedi 11 mai. L'ensemble des compagnies aériennes françaises est concerné. La progression des cours de l'or noir est également une mauvaise nouvelle pour les transporteurs aériens.
 """
spacy_streamlit.visualize(models, default_text)
#nlp = spacy.load("drop00")


#text=st.text_area('veuillez rentrer du texte')
#doc = nlp(text)
#print(doc)

