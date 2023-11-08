import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Input audio file path (replace with your audio file)
audio_file = "harvard.wav"

# Read the audio file
with sr.AudioFile(audio_file) as source:
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)

    # Listen for audio
    audio = recognizer.listen(source)

# Use Google Web Speech API for speech recognition
try:
    text = recognizer.recognize_google(audio)
    print("Transcription: " + text)

    # Save the transcription to a text file
    with open("transcription.txt", "w") as text_file:
        text_file.write(text)

    print("Transcription saved to transcription.txt")
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech API; {0}".format(e))
