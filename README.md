📚 ReadAndSpeak

ReadAndSpeak est une application Python qui permet de :

📖 Lire le contenu d’un fichier PDF

🔊 Le convertir en audiobook grâce à la synthèse vocale (Text-to-Speech)

🗣️ Reconnaître la voix de l’utilisateur pour convertir l’audio en texte (Speech-to-Text)

🚀 Objectifs du projet

Créer un outil pratique pour :

Écouter n’importe quel PDF (cours, livre, article…)

Transcrire des notes vocales en texte

Découvrir et pratiquer la gestion de projet Python (venv, Git, modules, etc.)

🔧 Fonctionnalités prévues

✅ Extraction du texte depuis un fichier PDF (pdfplumber)

⏳ Conversion du texte en audio (gTTS, pyttsx3, etc.)

⏳ Transcription de la voix en texte (SpeechRecognition, whisper, etc.)

⏳ Interface graphique simple avec Streamlit ou Tkinter

⏳ Option de sauvegarde des fichiers audio et texte

🛠️ Installation

Cloner le projet :

bash
Copier
Modifier
git clone https://github.com/ton-username/ReadAndSpeak.git
cd ReadAndSpeak
Créer un environnement virtuel :

bash
Copier
Modifier
python -m venv venv
# Windows :
venv\Scripts\activate
# macOS / Linux :
source venv/bin/activate
Installer les dépendances :

bash
Copier
Modifier
pip install -r requirements.txt
🗂️ Structure du projet

bash
Copier
Modifier
ReadAndSpeak/
├── main.py
├── venv/                   ← Environnement virtuel (non versionné)
├── requirements.txt        ← Bibliothèques installées
├── .gitignore              ← Fichiers exclus de Git
├── README.md               ← Description du projet
└── assets/                 ← (Optionnel) PDF, audios, tests
📌 To-Do

 Ajout du Text-to-Speech

 Ajout de la reconnaissance vocale

 Ajout d’une interface simple

 Lecture page par page

 Résumé automatique (bonus IA)

👤 Auteur
Ramy Garici
github.com/RamyGarici
