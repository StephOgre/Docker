import pandas as pd
import streamlit as st


df=pd.read_parquet("./comparaison_llama_mistral.parquet")
df.head()

#st.write("Voici les données complètes :")
#st.dataframe(df)

numero_texte = st.number_input(
    'Choisissez le numéro de texte (ligne) à afficher',
    value=1998
)

colonnes_selectionnees = st.multiselect(
    'Choisissez les colonnes à afficher',
    options=df.columns.tolist(),
    default=df.columns.tolist()
)

st.write(f"Affichage du texte numéro {numero_texte} :")
st.table(df.loc[(numero_texte - 1), colonnes_selectionnees])
