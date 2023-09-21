# Voice-to-Text-converter

Voice to Text converter :- In the above project I have made a voice to text converter using python language which will convert the spoken sentances into the written one

Libraries used :- 
1) speech_recognition = using this speech recognition we will fetch or recognize the speech of the user and using the fetched speech we will convert the speech into
text.
2) GTTS = Google Text to speech = in this gTts library the function of this library is to convert text to speech and speech to text this is developed by google
3) pygame = this library js used to greet the user with "enter the text you want to convert "

Initialize the game - we defined a function called initialize_pygame which uses the pygame library

The speak_text function takes a text string as input and converts it into speech.

We use the gTTS library to convert the input text to an audio file (in this case, "prompt.mp3").

The convert_spoken_to_text function handles the main logic for capturing spoken text and converting it to written text.
