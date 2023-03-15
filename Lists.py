import streamlit as st
from IPython.display import HTML

# Definiamo i generi musicali e le rispettive canzoni
music_genres = {
    "Pop": {
        "Dua Lipa - Levitating": "https://www.youtube.com/watch?v=TUVcZfQe-Kw",
        "Ariana Grande - positions": "https://www.youtube.com/watch?v=t9-iLYhyIgg",
        "Ed Sheeran - Shape of You": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
    },
    "Rock": {
        "Queen - Bohemian Rhapsody": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
        "The Rolling Stones - (I Can't Get No) Satisfaction": "https://www.youtube.com/watch?v=nrIPxlFzDi0",
        "Led Zeppelin - Stairway to Heaven": "https://www.youtube.com/watch?v=9Q7Vr3yQYWQ"
    },
    "Hip Hop": {
        "Kendrick Lamar - HUMBLE.": "https://www.youtube.com/watch?v=tvTRZJ-4EyI",
        "Drake - In My Feelings": "https://www.youtube.com/watch?v=DRS_PpOrUZ4",
        "Notorious B.I.G. - Juicy": "https://www.youtube.com/watch?v=_JZom_gVfuw"
    }
}

# Definiamo l'interfaccia utente di Streamlit
st.write("# Generi musicali")

# Creiamo una barra laterale per scegliere il genere musicale
selected_genre = st.sidebar.selectbox(
    "Scegli il genere musicale",
    list(music_genres.keys())
)

# Mostrare la canzone selezionata
if selected_genre in music_genres:
    st.write(f"## Canzoni {selected_genre}")
    selected_song = st.selectbox(
        "Scegli la canzone",
        list(music_genres[selected_genre].keys())
    )
    selected_song_url = music_genres[selected_genre][selected_song]
    st.write(f"### {selected_song}")
    st.write(f"Guarda il video su [YouTube]({selected_song_url})")
    HTML(f'<iframe width="560" height="315" src="{selected_song_url}" frameborder="0" allowfullscreen></iframe>')
else:
    st.write("Genere musicale non trovato")
