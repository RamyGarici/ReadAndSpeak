import streamlit as st
from pdf_reader import extract_text_from_pdf
from tts import tts
import pyttsx3,os,tempfile
text=""
engine=pyttsx3.init()
voices = engine.getProperty('voices')
voices_name=[f"{i} -> {voice.name} | {voice.languages}" for i, voice in enumerate(voices) if voice.languages is not None]


#Streamlit app setup
st.set_page_config(page_title="ReadAndSpeak", layout="centered")


st.title("📚 ReadAndSpeak")
st.header("🗣️ Text to Speech")
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
        try:
               tts(text, voice_index=voice_index)
        except Exception as e:
               st.error("❌ An error occurred during audio processing.")
       
    elif action == "💾 Save as audio":
        try:
            with tempfile.TemporaryDirectory() as tmpdirname:
                temp_path = os.path.join(tmpdirname, "speech.mp3")
                tts(text, voice_index=voice_index, save=True, filename=temp_path)

                with open(temp_path, "rb") as f:
                    audio_data = f.read()

                st.download_button("📥 Télécharger l'audio", data=audio_data, file_name="speech.mp3")
                st.success("✅ Audio prêt à être téléchargé !")
        except Exception as e:
            st.error("❌ Une erreur est survenue lors de la génération du fichier audio.")