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
    
    st.write("Total number of words:", len(word_count))
    st.write("Total number of unique words:", len(word_set))
    st.write("")
    st.write("10 most frequent words:")
    for word, count in top_words:
        st.write(f"{word}: {count}")
    
    word_set_df = pd.DataFrame(sorted(word_set), columns=['Parola'])
    word_set_df['Count'] = word_set_df['Word'].apply(lambda x: word_count[x])
    word_set_df = word_set_df.sort_values('Word')
    st.write("")
    st.write("All the words sorted:")
    st.write(word_set_df)

def main():
    st.title("Words counter")
    st.write("Inserisci here the text to analyze:")
    text = st.text_area("", height=200)
    if st.button("Words counter"):
        show_word_counts(text)

if __name__ == "__main__":
    main()
