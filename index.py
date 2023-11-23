#hello
# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
#importing web browser
import webbrowser
#importing os
import os
import pygetwindow as gw
import pyautogui
import random
from moviepy.editor import *




def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    text_to_speech=pyttsx3.init()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening.')
        r.adjust_for_ambient_noise(source)
        
        r.pause_threshold = 0.5
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query
    
# creating Speak() function to giving Speaking power
# to our voice assistant 
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()



# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    myweb=["youtube","skillrack","facebook"]
    mysystem=["open calculator","open word","open powerpoint","open wordpad"]
    myclose=["close calculator","close word","close wordpad","close powerpoint"]
    jokes = [
    "In Which city always have power of 24/7 h? The city name is Electricity",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    " What is brown, hairy and wears sunglasses? A coconut on vacation.",
    "Where did the music teacher leave her keys? In the piano!",
    "What do you call a guy who’s really loud? Mike.",
    "Why do birds fly south in the winter? It’s faster than walking!",
    "Why is a football stadium always cold? It has lots of fans!",
    ]
    while True:
        commanded = take_commands()
        command=commanded.lower()
        if "exit" in command:
            Speak("Sure sir! as your wish, bye")
            break
        if(command in mysystem):
            match command:
                case "open calculator":
                    Speak("Opening Calculator")
                    os.system("calc.exe")
                case "open wordpad":
                    Speak("Opening Wordpad")
                    os.system("write.exe")   
                case "open word":
                    Speak("opening word")
                    os.system("start winword")
                case "open powerpoint":
                    Speak("opening powerpoint")
                    os.system("start powerpnt")    
            
        if command in myweb:
            match command:
                case "youtube":
                    Speak("Openning Youtube")
                    webbrowser.open("https://youtube.com/" )
                case "skillrack":
                    Speak("Openning SkiiRack")
                    webbrowser.open("https://www.skillrack.com/")
                case "facebook":
                    Speak("Openning FaceBook")
                    webbrowser.open("https://www.facebook.com/")
        if(command in myclose):
            match command:
                case "close calculator":
                    calculator_window = gw.getWindowsWithTitle("Calculator")
                    if calculator_window:
                        calculator_window[0].close()
                        Speak("Calculator closed.")
                    else:
                        Speak("Calculator window not found.")
                case "close wordpad":
                    wordpad_window = gw.getWindowsWithTitle("Wordpad")
                    if wordpad_window:
                        wordpad_window[0].close()
                        Speak("wordpad closed.")
                    else:
                        Speak("wordpad window not found.")
                case "close word":
                    word_window = gw.getWindowsWithTitle("Word")
                    if word_window:
                        word_window[0].close()
                        Speak("word closed.")
                    else:
                        Speak("word window not found.")
                case "close powerpoint":
                    pnt_window = gw.getWindowsWithTitle("Powerpoint")
                    if pnt_window:
                        pnt_window[0].close()
                        Speak("powerpoint closed.")
                    else:
                        Speak("powerpoint window not found.")

        if "close youtube" in command:
            tab_title_to_close = "YouTube"
            windows = gw.getWindowsWithTitle(tab_title_to_close)
            if windows:
                windows[0].activate()
                pyautogui.hotkey('ctrl', 'w')
                print("closing youtube")
        if "tell me a joke" in command:
            random_joke = random.choice(jokes)
            print(random_joke)
            Speak(random_joke)
        if "play games" in command:
            import cricket
        if "search" in command:
            
            import search 
            
        if "open camera" in command:
            import camera    
        if "take screenshot" in command:
                # Capture a screenshot
                screenshot = pyautogui.screenshot()

                # Save the screenshot to a file
                screenshot.save("screenshot.png")

                print("Screenshot captured and saved as screenshot.png")
        if "convert video to audio" in command:
            import video_to_audio   
        if "convert audio to text" in command:
            import transcript
        if "convert speech to audio" in command:
            import speech_to_audio
        if "convert audio to synopsis"  in command:
            import text  

            
                     
                
        else:
            print("Command not recognized.")











            
            

        
                      
            
            

            
