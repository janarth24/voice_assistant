import cv2
import speech_recognition as sr

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Open the camera
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open the camera")
else:
    print("Say 'Capture' to take a photo or 'Close camera' to close the camera...")

    while True:
        # Capture audio from the microphone
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        
        try:
            print("Camera Listening...")
            # Recognize speech using Google Speech Recognition
            command = recognizer.recognize_google(audio).lower()
            
            print("You said:", command)
            
            if "capture" in command:
                # Capture a frame from the camera
                ret, frame = camera.read()
                
                # Save the captured photo
                if ret:
                    cv2.imwrite("captured_photo.jpg", frame)
                    print("Photo captured and saved as captured_photo.jpg")
                else:
                    print("Error: Failed to capture a photo")
            
            if "close camera" in command:
                break  # Exit the loop to close the camera
        
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

        # Display the frame in a window
        ret, frame = camera.read()
        cv2.imshow("Camera Feed", frame)

        # Exit when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
