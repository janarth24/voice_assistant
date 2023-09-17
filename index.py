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

def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
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
    while True:
        commanded = take_commands()
        command=commanded.lower()
        if "exit" in command:
            Speak("Sure sir! as your wish, bai")
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
                    
            Speak("You can get this code from c") 
           # url="https://youtube.com/"   
            
            

            
