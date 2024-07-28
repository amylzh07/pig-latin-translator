# Amy Zhang
# Computer Science 20
# June 4, 2024
# Pig Latin Translator Assignment

import streamlit as st

VOWELS = "aeiouy"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"

def get_prefix(some_word):
    prefix = ""
    for index in range(len(some_word)):
        if some_word[index] in VOWELS:
            prefix = some_word[:index]
            return prefix
    
def get_stem(some_word):
    stem = ""
    for index in range(len(some_word)):
        if some_word[index] in VOWELS:
            stem = some_word[index:]
            return stem

def translate_word(some_word):
    if some_word[0].isupper() == True:
        is_uppercase = True
    else:
        is_uppercase = False
        
    some_word = some_word.casefold()
    
    if some_word[0] in VOWELS:
        translated_word = f"{some_word}yay"
        if is_uppercase == True:
            translated_word = translated_word.capitalize()
        return translated_word
    
    elif some_word[0] in ALPHABET:
        prefix = get_prefix(some_word)
        stem = get_stem(some_word)
        translated_word = f"{stem}{prefix}ay"
        if is_uppercase == True:
            translated_word = translated_word.capitalize()
        return translated_word
    
def translate_sentences(some_sentence):
    the_words = some_sentence.split()
    
    the_sentence = []
    
    for word in the_words:
        word_to_translate = ""
        punctuation = ""
        the_number = ""
        for char in word:
            if char in ALPHABET or char in ALPHABET.upper():
                word_to_translate = word_to_translate + char
            elif char in NUMBERS:
                the_number = the_number + char
            else:
                punctuation = char
                
        if the_number != "":
            the_sentence.append(the_number)
        else:
            the_sentence.append(f"{translate_word(word_to_translate)}{punctuation}")
                        
    translated_sentence = " ".join(the_sentence)
    
    return translated_sentence
   
st.title("Pig Latin Translator")
st.subheader("On behalf of the de facto embassy of Saskatoon, we would like to extend our warmest welcome to visiting officers from Vatican City.")

user_sentence = st.text_input("Enter an English sentence to be converted into Pig Latin: ")
translated_sentence = translate_sentences(user_sentence)
st.write(translated_sentence)

with open("translation_history.txt", "a") as translation_history:
    translation_history.write(f"{user_sentence} \n")
    translation_history.write(f"{translated_sentence} \n")

