import speech_recognition as sr
from gtts import gTTS
import os

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError as e:
            return f"Error with the speech recognition service: {e}"

def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # for Windows

def assistant():
    print("Hello! I'm your voice assistant.")
    while True:
        command = listen().lower()

        if 'exit' in command:
            print("Goodbye!")
            break

        response = "I didn't catch that. Can you repeat?"
        if 'hello' in command:
            response = "Hello! How can I assist you today?"

        speak(response)

if __name__ == "__main__":
    assistant(
