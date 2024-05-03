import streamlit as st
# from gensim.summarization import summarize
import spacy
import spacy_streamlit
from nltk.corpus import wordnet
from textblob import TextBlob
#from pattern.web import Google
import streamlit.components.v1 as components
from pattern.en import pluralize , singularize,comparative, superlative
import torch
import codecs
import os
from dotenv import load_dotenv

load_dotenv()

import openai
nlp = spacy.load('en_core_web_sm')

#key = os.environ.get("OPENAI_API_KEY")
key="sk-proj-ChhIZz23rnQztlZFKZVtT3BlbkFJDXBJjIYqFE0XrFH6AVdW"
#custom funtion 
def summary(text):
    openai.api_key = key
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=f"Summarize the following text:\n{text}",
        max_tokens=512,
    )
    return(response.choices[0].text)

def meaning(text):
    openai.api_key = key
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=f"Give me 5 synonyms for the following text: \n{text}",
        max_tokens=512,
    )
    return(response.choices[0].text)

def definition(text):
    openai.api_key = key
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=f"Give me a very short definition for the following text: \n{text}",
        max_tokens=512,
    )
    return(response.choices[0].text)

def example(text):
    openai.api_key = key
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=f"Give me a example sentence for the following text: \n{text}",
        max_tokens=512,
    )
    return(response.choices[0].text)

def translate(text, a):
    openai.api_key = key
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
        prompt=f"Translate the following text {text} to {a}", 
        max_tokens=512,
    )
    return(response.choices[0].text)
        


# Custom Components Fxn
def st_calculator(calc_html,width=1000,height=1350):
	calc_file = codecs.open(calc_html,'r')
	page = calc_file.read()
	components.html(page,width=width,height=height,scrolling=False)
    
#main

def main():
    activites = ["Summary","Tokenizer","Synonyms","Translator","Search","Spell Correction"]
    choice = st.sidebar.selectbox("Select Activity",activites)
    if choice == "Summary":
        html_temp = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Text Summarizer</p></div>
	"""
        components.html(html_temp)
        # text = st.text_area("Input Text For Summary",height=300)
       
        # text_range= st.sidebar.slider("Summarize words Range",25,500)
        text = st.text_area("Input Text For Summary",height=250)
        if st.button("Summarize"):
            st.success(summary(text))
        #if st.button("summarize"):
           #st.warning(summary(text,word_count=text_range))
    # Tokenizer 
    elif choice == "Tokenizer":
        html_temp1 = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Text Tokenizer</p></div>
	"""
        components.html(html_temp1)
        row_data = st.text_area("Write Text For Tokenizer")
        docx= nlp(row_data)
        if st.button("Tokenizer"):
            spacy_streamlit.visualize_tokens(docx,attrs=['text','pos_','dep_','ent_type_'])
        if st.button("NER"):
            spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)
        if st.button("Text Relationship"):
            spacy_streamlit.visualize_parser(docx)
       # synonyms      
    elif choice == "Synonyms":
        html_temp2 = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Words Synonyms</p></div>
	""" 
        components.html(html_temp2)
        text = st.text_area("Enter Text")
        if st.button("Find"):
                st.success(meaning(text))
        if st.checkbox("Defination"):
            st.warning(definition(text)) 
        if st.checkbox("Example"):
            st.success(example(text))
        
      # Translator          
    elif choice == "Translator":
        html_temp3 = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Text Translator</p></div>
	""" 
        components.html(html_temp3)
        row_text = st.text_area("Enter Your Text For Translation",height=300)
        # translation_text = TextBlob(row_text)
        list1 = ["Hindi","Marathi","German","French","Spanish","Tamil","Japanese"]
        a = st.selectbox("select",list1)
        if st.button("search"):
            #input1 = TextBlob("Simple is better than complex")
            st.success(translate(row_text, a))
    #Search Bar
    elif choice == "Search":
        html_temp4 = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;,text-align:center;">Search Bar</p></div>
	""" 
        components.html(html_temp4)
        row_text= st.text_input("Search Anything")
        google = Google(license=None)
        if st.button("search"):
            for search_result in google.search(row_text):
                st.write(search_result.text)
                st.warning(search_result.url)
    elif choice == "Spell Correction":
        html_temp6 = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Spell Correction</p></div>
	"""
        components.html(html_temp6)
        text_data = st.text_area("Enter Text Here")
        a = TextBlob(text_data)
        if st.button("Correct"):
            st.success(a.correct())
        html_temp7 = """
	<div style="background-color:tomato;"><p style="color:white;font-size:60px;,text-align:center;">pluralize & singularize</p></div>
	"""
        components.html(html_temp7)
        text_data1 = st.text_input("Enter a word For pluralize / singularize")
        if st.checkbox("Pluralize"):
            st.warning(pluralize(text_data1))
        if st.checkbox("singularize"):
            st.warning(singularize(text_data1))
        
        html_temp8 = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;,text-align:center;">comparative & superlative</p></div>
	""" 
        components.html(html_temp8)
        text2 = st.text_input("Enter Text For comparative & superlative")
        if st.checkbox("comparative"):
            st.success(comparative(text2))
        if st.checkbox("superlative"):
            st.success(superlative(text2))
        
          
if __name__ == '__main__':
    main()

