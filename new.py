import speech_recognition as sr
from gtts import gTTS
import pygame

def initialize_pygame():
    pygame.mixer.pre_init(44100, -16, 2, 2048)  # Initialize the mixer
    pygame.init()  # Initialize Pygame

def speak_text(text):
    # Use gTTS to convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save("prompt.mp3")

    # Play the generated audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load("prompt.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.event.wait()

def convert_spoken_to_text():
    # Initialize Pygame
    initialize_pygame()

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Speak a prompt
    speak_text("Please speak the text you want to convert to written text...")

    # Capture audio from the microphone
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        # Use Google Speech Recognition to convert audio to text
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition; {0}".format(e))

if __name__ == "__main__":
    convert_spoken_to_text()
