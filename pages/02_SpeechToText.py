import streamlit as st
import pyttsx3,os,tempfile
import speech_recognition as sr


st.title("🗣️ Speech to Text")

if st.button("🎙️ Parler maintenant"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Parle maintenant...")
        audio = recognizer.listen(source)

        with st.spinner("🧠 Transcription en cours..."):
            try:
                text = recognizer.recognize_google(audio, language="fr-FR")
                st.success("✅ Transcription réussie !")
                st.text_area("📝 Résultat :", value=text, height=200)
            except sr.UnknownValueError:
                st.error("❌ Google n'a pas compris l'audio.")
            except sr.RequestError as e:
                st.error(f"❌ Erreur de requête : {e}")
    if text is not None:
        transcription= text.encode('utf-8')
                
        st.download_button("📥 Télécharger la transcription", 
                           data=transcription, 
                           file_name="transcription.txt")
