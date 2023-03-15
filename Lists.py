import streamlit as st

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
    "Select the musical Genre you want to listen to: ",
    list(music_genres.keys())
)

# Mostrare la canzone selezionata
if selected_genre in music_genres:
    st.write(f" {selected_genre} ## Songs")
    selected_song = st.selectbox(
        "Select the song",
        list(music_genres[selected_genre].keys())
    )
    selected_song_url = music_genres[selected_genre][selected_song]
    st.write(f"### {selected_song}")
    st.write(f"Listen the song on[YouTube]({selected_song_url})")
else:
    st.write("Music genre not found :(")
