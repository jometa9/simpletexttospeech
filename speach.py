from google_speech import Speech
text ="your text here"
lang = "es"
speech = Speech(text, lang)
speech.save("audio.mp3")