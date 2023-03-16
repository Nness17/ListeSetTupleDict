import streamlit as st

# Definiamo i generi musicali e le rispettive canzoni
music_genres = {
    "Rosa Chemical": {
        "Made In Italy (Sanremo 2023) prod. BDope - Rosa Chemical": "https://youtu.be/UQuoY73tUsw",
        "Polka 3 prod. BDope - Rosa Chemical": "https://youtu.be/vu8DDbY0jZA",
        "britney ;-) ft. MamboLosco, Radical - Rosa Chemical": "https://youtu.be/76Zny0XaV6Q",
        "LA CANZONE NOSTRA ft. MACE, Salmo - BLANCO": "https://youtu.be/XE6lV6xseQ4",
        "L'Isola delle Rose - BLANCO": "https://youtu.be/g2647z7McDE"
    },
    "BLANCO": {
        "Notti in Bianco - BLANCO": "https://youtu.be/wppn2Via-Tk",
        "Mi fai impazzire ft. Sfera Ebbasta - BLANCO": "https://youtu.be/FJNOkLCIg5Y",
        "Finchè non mi seppelliscono - BLANCO": "https://youtu.be/7p09c3GgF4A",
        "LA CANZONE NOSTRA ft. MACE, Salmo - BLANCO": "https://youtu.be/XE6lV6xseQ4",
        "L'Isola delle Rose - BLANCO": "https://youtu.be/g2647z7McDE"
    },
    "Guè": {
        "Mollami pt.2 - Guè": "https://youtu.be/ab4PdCyqbTI",
        "Scooteroni RMX ft. Sfera Ebbasta - Marracash & Guè": "https://youtu.be/j3FXV0Ma3QA",
        "Lamborghini (RMX) ft. Sfera Ebbasta, Elettra Lamborghini": "https://youtu.be/DkXgmrGlpjQ",
        "Cookies N' Cream ft. ANNA, Sfera Ebbasta": "https://youtu.be/z_D_SP5YGh0",
        "Salvador Dalì - Marracash & Guè": "https://youtu.be/rlaTV5MQTQY"
    },
    "Marracash": {
        "Crudelia - I nervi - Marracash": "https://youtu.be/M8C_aieRM4Q",
        "Crazy Love - Marracash": "https://youtu.be/JHqxzM2tZHs",
        "∞ LOVE ft. Guè - Marracash": "https://youtu.be/RN4zhaQEa7I",
        "Nemesi ft. BLANCO - Marracash": "https://youtu.be/3pVCFx1kptk",
        "Bravi a cadere - I polmoni - Marracash": "https://youtu.be/hPjV6yu4HW4"
    },
    "Shiva": {
        "Non lo sai - Shiva": "https://youtu.be/gbcYVcAaIIc",
        "Alleluia ft. Sfera Ebbasta - Shiva": "https://youtu.be/nZdNV5PnZws",
        "TAKE 4 - Shiva": "https://youtu.be/dWcipGS717Q",
        "Aston Martin ft. Headie One - Shiva": "https://youtu.be/sBtYmYTD2d0",
        "Vorrei ft. Lazza - Shiva": "https://youtu.be/_mkIGhbeMLM"
    },
    "Ghali": {
        "Wily Wily - Ghali": "https://youtu.be/QqbJt1qnXTQ",
        "Habibi - Ghali": "https://youtu.be/fgt6luBwzz0",
        "Dende - Ghali": "https://youtu.be/wkSgZ9WDlPs",
        "Peace & Love ft. Sfera Ebbasta, Charlie Charles - Ghali": "https://youtu.be/PxQVexjVlg4",
        "Boogieman ft. Salmo - Ghali": "https://youtu.be/-7lqGbIE3aM"
    },
    "Fabri Fibra": {
        "Tranne te - Fabri Fibra": "https://youtu.be/qrM0z3v3LUY",
        "Applausi per Fibra - Fabri Fibra": "https://youtu.be/Ji8RqJGEiI8",
        "Fenomeno - Fabri Fibra": "https://youtu.be/EJmRU9vOsgo",
        "Propaganda ft. Colapesce, Dimartino": "https://youtu.be/VZgtEU4B70o",
        "Pamplona ft. TheGiornalisti": "https://youtu.be/84aJv0NelEU"
    },
    "Nitro": {
        "Storia di un defunto artista - Nitro": "https://youtu.be/3GsfoK-s3Ww",
        "Rotten - Nitro": "https://youtu.be/-uSp26jdilA",
        "Chairaggione ft. Salmo - Nitro": "https://youtu.be/B3z388S9iPU",
        "Pleasantville - Nitro": "https://youtu.be/O5JZ8kfbZ0A",
        "Trankilo ft. Vegas Jones - Nitro": "https://youtu.be/h-Aqys9MfoQ"
    },
    "Izi": {
        "Chic - Izi": "https://youtu.be/HFqstkhwFho",
        "Aeroplanini di carta ft. Rkomi - Izi": "https://youtu.be/SnKvCdI5Hag",
        "Wild Bandana ft. Tedua, Vaz Tè": "https://youtu.be/B3z388S9iPU",
        "48H - Izi": "https://youtu.be/PCWFsVmT144",
        "Tutto apposto ft. Sfera Ebbasta - Izi": "https://youtu.be/npW2okHL_0A"
    },
    "Gemitaiz & MadMan": {
        "Veleno 6 - Gemitaiz & MadMan": "https://youtu.be/9jDw0vaA__g",
        "Veleno 7 - (Prod. Mixer T, PK) - Gemitaiz & MadMan": "https://youtu.be/ykGRZ4Li3OU",
        "Veleno 8 - Gemitaiz & MadMan": "https://youtu.be/059sh0cmm-0",
        "Senza di me ft. Venerus & FRANCO126 - Gemitaiz",
        "Toradol - Gemitaiz": "https://youtu.be/mllaiuAEeqg",
        "Bolla Papale FST - MadMan": "https://youtu.be/TvnTUOjgGyQ",
        "Dopperlganger - MadMan": "https://youtu.be/tN_b7VT9U2w"
    },
    "Sfera Ebbasta": {
        "Tran Tran - Sfera Ebbasta": "https://youtu.be/tU_KbOs8w2o",
        "Italiano Anthem - Sfera Ebbasta, Rvssian": "https://youtu.be/vUYn-mWkHXQ",
        "Tik Tok RMX (feat. Marracash, Guè Pequeno, Paky & Geolier) - Sfera Ebbasta": "https://youtu.be/R_vhQyDkL1E",
        "Famoso - Sfera Ebbasta": "https://youtu.be/fF84WK6KBgA",
        "Sciroppo ft DrefGold (Prod. Charlie Charles, Daves The Kid) ft. DrefGold - Sfera Ebbasta": "https://youtu.be/6BCpyH1ZNZE"
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
