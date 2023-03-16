import streamlit as st
import pandas as pd

def count_words(text):
    """
    Questa funzione prende in input un testo e restituisce un dizionario
    che associa ad ogni parola nel testo il numero di volte che compare.
    """
    words = text.lower().split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def show_word_counts(text):
    """
    Questa funzione prende in input un testo e mostra una tabella con le parole
    più frequenti e il numero di volte che compaiono, utilizzando tuple, sets e dictionary.
    """
    word_count = count_words(text)
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_word_count[:10]
    word_set = set(word_count.keys())
    
    st.write("Numero totale di parole:", len(word_count))
    st.write("Numero di parole uniche:", len(word_set))
    st.write("")
    st.write("10 parole più frequenti:")
    for word, count in top_words:
        st.write(f"{word}: {count}")
    
    word_set_df = pd.DataFrame(sorted(word_set), columns=['Parola'])
    word_set_df['Conteggio'] = word_set_df['Parola'].apply(lambda x: word_count[x])
    word_set_df = word_set_df.sort_values('Parola')
    st.write("")
    st.write("Tutte le parole ordinate:")
    st.write(word_set_df)

def main():
    st.title("Contatore di parole")
    st.write("Inserisci il testo da analizzare:")
    text = st.text_area("", height=200)
    if st.button("Conta parole"):
        show_word_counts(text)

if __name__ == "__main__":
    main()
