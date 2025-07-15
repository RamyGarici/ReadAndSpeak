import pyttsx3
# Choose a voice
def choose_voice_interactively(voices):
    
    for i, voice in enumerate(voices):
        print(f"{i} → {voice.name} | {voice.languages}")
    index = int(input("Choisissez l’index de la voix : "))
    return index

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
