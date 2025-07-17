import pyttsx3


# Convert text to speech using the selected voice
def tts(text,save=False,filename="output.mp3",voice_index=0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
   
    
    engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('rate', 150) 
    if save:
        engine.save_to_file(text,filename)
    else:
        engine.say(text)
    engine.runAndWait()
    engine=None
