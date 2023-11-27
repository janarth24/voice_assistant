import speech_recognition as sr
import pygetwindow as gw

# Initialize the recognizer
r = sr.Recognizer()

# Function to close Google Chrome
def close_google_chrome():
    try:
        # Get the window by title (assuming the title is "Google Chrome")
        chrome_window = gw.getWindowsWithTitle("Google Chrome")[0]

        # Close the window
        chrome_window.close()
        print("Closed Google Chrome successfully.")
    except IndexError:
        print("Google Chrome window not found.")

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say 'close Google Chrome' to close the browser:")

    # Adjust for ambient noise for better recognition
    r.adjust_for_ambient_noise(source)

    # Listen for audio input
    audio = r.listen(source)

    print("Recognizing...")

    try:
        # Recognize speech using Google Speech Recognition
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")

        # Check if the command contains "close Google Chrome"
        if "close google chrome" in command:
            close_google_chrome()
        else:
            print("Command not recognized as 'close Google Chrome'.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")
