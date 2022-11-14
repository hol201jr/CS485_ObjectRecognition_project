import cv2 
import pyttsx3
import time
import speech_recognition as sr

def sayWord(word,num):
    print(word)
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()
    time.sleep(num)

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

cap = cv2.VideoCapture(0)
engine = pyttsx3.init()
eng = pyttsx3.init()
voice = eng.getProperty('voices')
engine.setProperty('voice', voice[1].id)
found = 1

sayWord("Welcome to our app.",1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

sayWord("Would you like to start, object recognition?",1)
sayWord("Press y for yes, or n for no.",1)


print("Press y for yes or n for no: ")
response = input()



if response == 'y':
    sayWord("Activating object recognition software.",2)

    engine.say("To deactivate application press q, otherwise always point camera forward.",2)
    engine.runAndWait()

    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3 , 5)
    
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0),2)

            if(found == 1):
                print("Found Chair")
                sayWord("Watch out! There is a person up ahead!",1)
                found = 0
            time.sleep(1)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sayWord("Turning off App.",1)
            break

elif response == 'n':
    sayWord("You are about to add a new object, to the database.",1)
    #Prepare Camera for object snap
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    #Initialize voice recognizer
    r = sr.Recognizer()
    result, image = cam.read()

    if result:
        try:
            sayWord("What is the name of the object?",1)
            sayWord("Please say the name.",0)
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio = r.listen(source2)

                obj = r.recognize_google(audio)
                obj = obj.lower()

                print("Text to speech ", obj)
                SpeakText(obj)
                filename = obj + ".jpg"
                print(filename)
                
                sayWord("Hold the camera steady, infront of you.",1)
                time.sleep(3)
                cv2.imshow(filename, image)
                
                sayWord("Taking picture in 3, 2, 1.",1)
                
                cv2.imwrite(filename, image)
                
                sayWord("Press q to exit.",0)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows
        except sr.RequestError as e:
            sayWord("Could not request result; {0}")
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")

cap.release()
cv2.destroyAllWindows()