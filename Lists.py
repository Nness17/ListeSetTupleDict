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
    "Sfera Ebbasta": {
        "Tran Tran - Sfera Ebbasta": "https://youtu.be/tU_KbOs8w2o",
        "Italiano Anthem - Sfera Ebbasta, Rvssian": "https://youtu.be/vUYn-mWkHXQ",
        "Tik Tok RMX (feat. Marracash, Guè Pequeno, Paky & Geolier) - Sfera Ebbasta": "https://youtu.be/R_vhQyDkL1E",
        "Famoso - Sfera Ebbasta": "https://youtu.be/fF84WK6KBgA",
        "Sciroppo ft DrefGold (Prod. Charlie Charles, Daves The Kid) ft. DrefGold - Sfera Ebbasta": "https://youtu.be/6BCpyH1ZNZE"
        }
    },
    "Lazza": {
        "OUV3RTURE - Lazza": "https://www.youtube.com/watch?v=TTxqCWGBYhg",
        "Cenere - Lazza": "https://youtu.be/A5ab7U9RVLE",
        "J - Lazza": "https://youtu.be/vgZoXnrN_eI",
        "Alibi - Lazza": "https://youtu.be/vzHuYaS6Iio",
        "SENZA RUMORE - Lazza": "https://youtu.be/dJmaFREMVnw"
    }     
}

# Definiamo l'interfaccia utente di Streamlit
st.write(f"##ITALIAN MUSIC")

# Creiamo una barra laterale per scegliere il genere musicale
selected_genre = st.sidebar.selectbox(
    "Select the musical Genre you want to listen to: ",
    list(music_genres.keys())
)

# Mostrare la canzone selezionata
if selected_genre in music_genres:
    st.write(f"## {selected_genre}")
    selected_song = st.selectbox(
        "Select the song",
        list(music_genres[selected_genre].keys())
    )
    selected_song_url = music_genres[selected_genre][selected_song]
    st.write(f"### {selected_song}")
    st.write(f"Listen the song on [YouTube]({selected_song_url})")
else:
    st.write("Music genre not found :(")
