import streamlit as st
from pdf_reader import extract_text_from_pdf
from tts import tts
import pyttsx3
text=""
engine=pyttsx3.init()
voices = engine.getProperty('voices')
voices_name=[f"{i} -> {voice.name} | {voice.languages}" for i, voice in enumerate(voices) if voice.languages is not None]


#Streamlit app setup
st.set_page_config(page_title="ReadAndSpeak", layout="centered")

st.title("📚 ReadAndSpeak")
st.write("Convert a PDF into speech or save it as an audio file.")
upload_file=st.file_uploader("Upload a PDF file", type=["pdf"])
if upload_file is not None:
    text=extract_text_from_pdf(upload_file)
    

st.text_area("📖 Extracted Text", value=text, height=300)
st.write("What would you like to do?")
action = st.radio("Action", ["🔊 Read aloud", "💾 Save as audio"])
voice_index = st.selectbox("🎙️ Choose a voice", options=range(len(voices)), format_func=lambda i: voices_name[i])
if st.button("▶️ Go"):
    
    if action == "🔊 Read aloud" :
        tts(text=text,voice_index=voice_index)
    elif action== "💾 Save as audio":
        tts(text,save=True)
        st.success("Audio saved successfully!")
     