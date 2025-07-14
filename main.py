from pdf_reader import extract_text_from_pdf
from tts import tts

pages=extract_text_from_pdf("../../dummy.pdf")

for page in pages:
    text = page.extract_text()
    if text:
       choice=input("Do you want to save the audio? (yes/no): ")
       if choice.lower() == 'yes':
            tts(text,save=True) 
