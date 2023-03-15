import streamlit as st

# Definisci i generi musicali e le loro canzoni
generi_musicali = {
    'Rock': [
        ('Queen', 'Bohemian Rhapsody', 'https://www.youtube.com/watch?v=fJ9rUzIMcZQ'),
        ('Led Zeppelin', 'Stairway to Heaven', 'https://www.youtube.com/watch?v=9Q7Vr3yQYWQ'),
        ('Pink Floyd', 'Comfortably Numb', 'https://www.youtube.com/watch?v=_FrOQC-zEog')
    ],
    'Pop': {
        ('Michael Jackson', 'Thriller', 'https://www.youtube.com/watch?v=4V90AmXnguw'),
        ('Madonna', 'Like a Virgin', 'https://www.youtube.com/watch?v=s__rX_WL100'),
        ('Whitney Houston', 'I Will Always Love You', 'https://www.youtube.com/watch?v=3JWTaaS7LdU')
    },
    'Hip Hop': {
        ('Tupac', 'California Love', 'https://www.youtube.com/watch?v=5wBTdfAkqGU'),
        ('Notorious B.I.G.', 'Juicy', 'https://www.youtube.com/watch?v=_JZom_gVfuw'),
        ('Nas', 'NY State of Mind', 'https://www.youtube.com/watch?v=UKjj4hk0pV4')
    }
}

# Crea una lista con tutti i nomi delle canzoni utilizzando un set comprehension
canzoni = {canzone for genere in generi_musicali for artista, canzone, link in generi_musicali[genere]}

# Definisci la barra laterale per selezionare il genere musicale
genere_selezionato = st.sidebar.selectbox(
    'Seleziona il genere musicale',
    list(generi_musicali.keys())
)

# Crea una lista con tutte le canzoni del genere selezionato utilizzando una tuple e list comprehension
canzoni_genere_selezionato = [canzone[1] for canzone in generi_musicali[genere_selezionato]]

# Definisci la sezione principale della pagina
st.title('Generi musicali')
st.write(f'Selezionato: {genere_selezionato}')
st.write(f'Canzoni: {", ".join(canzoni_genere_selezionato)}')

# Crea una lista con tutte le canzoni del genere selezionato e i link a YouTube utilizzando una lista comprehension
canzoni_e_link = [f'{canzone} - {artista} ({link})' for artista, canzone, link in generi_musicali[genere_selezionato]]

# Mostra la lista di canzoni e link nella sezione principale
st.write('Canzoni e link a YouTube:')
for canzone in canzoni_e_link:
    st.write(canzone)
