import streamlit as st

# Creiamo una lista di frutti
fruits = ["mela", "banana", "kiwi", "ananas", "arancia"]

# Creiamo una tupla di città
cities = ("Roma", "Milano", "Napoli", "Torino", "Firenze")

# Creiamo un set di numeri
numbers = {1, 2, 3, 4, 5}

# Creiamo un dizionario di colori
colors = {"rosso": "#FF0000", "verde": "#00FF00", "blu": "#0000FF"}

# Definiamo l'interfaccia utente di Streamlit
st.write("# Utilizzo di liste, tuple, set e dizionari in Python")

# Creiamo una barra laterale per scegliere cosa stampare
selected_option = st.sidebar.selectbox(
    "Cosa vuoi stampare?",
    ("Frutti", "Città", "Numeri", "Colori")
)

# Mostriamo la lista di frutti
if selected_option == "Frutti":
    st.write("### Lista di frutti")
    for fruit in fruits:
        st.write(fruit)

# Mostriamo la tupla di città
elif selected_option == "Città":
    st.write("### Tupla di città")
    for city in cities:
        st.write(city)

# Mostriamo il set di numeri
elif selected_option == "Numeri":
    st.write("### Set di numeri")
    for number in numbers:
        st.write(number)

# Mostriamo il dizionario di colori
else:
    st.write("### Dizionario di colori")
    for key, value in colors.items():
        st.write(f"{key}: {value}")
