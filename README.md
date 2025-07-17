📚 ReadAndSpeak
ReadAndSpeak is a Python Streamlit application that allows you to:

📖 Read and extract text from PDF files

🔊 Convert extracted text into audio using Text-to-Speech (TTS)

🗣️ Convert your voice into text using Speech Recognition (Speech-to-Text)

🚀 Project Goals
Listen to any PDF (e.g., books, courses, articles) as audio

Transcribe voice notes into text

Practice Python modular project structure (virtual environment, Streamlit pages, Git)

🛠️ Installation
Clone the repository:


git clone https://github.com/your-username/ReadAndSpeak.git
cd ReadAndSpeak
Create a virtual environment:


python -m venv venv
Activate the virtual environment:

On Windows:


venv\Scripts\activate
On macOS/Linux:


source venv/bin/activate
Install dependencies:


pip install -r requirements.txt

streamlit  run TextToSpeech.py
🗂️ Project Structure

ReadAndSpeak/
├── pdf_reader.py          # Handles text extraction from PDF files
├── TextToSpeech.py        # Converts text to speech (TTS)
├── tts.py                 # (Optional) Shared TTS utilities
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── pages/
│   └── 02_SpeechToText.py # Page for speech-to-text functionality
✅ Features Completed
 PDF text extraction

 Text-to-Speech with audio playback

 Speech-to-Text using microphone input

 Streamlit UI with sidebar navigation

 Downloadable transcript or audio

📌 Upcoming Features
 Page-by-page PDF reading

 Automatic summarization with AI (bonus)

 Dark mode

 Audio file upload and transcription

👤 Author
Ramy Garici
🔗 github.com/RamyGarici

