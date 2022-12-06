#Title: Object Recognition.py
#Authors: Manuel Holguin, Derek Oda, Seth Ball, Gabe Romero
#Date: 12-05-2022
#Description: Python implementation of object recognition
#       for CS485. Announciates process with pyttsx3
#       uses object recognition using OpenCV to dectect object
#       (Could not train in time imported face recognition file 
#       from internet source Author: Rainer Lienhart)
#       App has a secondary option that takes a picture of an object
#       and stores the image in the folder to eventually add to a DB for
#       training.

import cv2 #import statement for computer Vision
import pyttsx3 #Import for Audio feedback
import time # Import for time handleling in Program
import speech_recognition as sr #Speech recognition for user input

#Speech Functions uses across the program
#Implemented to assist the visually impared
#sayWord @param takes a string and int as input
#int is used to slow down the procress for the user.
def sayWord(word,num):
    print(word)
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()
    time.sleep(num)
#Speech to text function Used for object creation
#into the databse. With the assumption user has
#Visual impairment and cannot type into the device
#accuratly.
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#Initialize camera capture
#Rev up speech engine to vocalize commands to the user
cap = cv2.VideoCapture(0)
engine = pyttsx3.init()
eng = pyttsx3.init()

#Selects voice for sound feedback
voice = eng.getProperty('voices')
engine.setProperty('voice', voice[1].id)

#Found flag if object is found to stop device from
#repeating object found repeated times.
found = 1

#start of program
sayWord("Welcome to our app.",1)

#Load training library for Object
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Ask user for input
sayWord("Would you like to start, object recognition?",1)
sayWord("Press y for yes, or n for no.",0)
print("Press y for yes or n for no: ")
response = input()


#If response is y then begin Object recognition portion
if response == 'y':
    sayWord("Activating object recognition software.",2)
    sayWord("To deactivate application press q, otherwise always point camera forward.",2)

    #Continuosly refresh camera for video feedback
    while(True):
        #Camera get frame and return value from camera
        ret, frame = cap.read()

        #set color feedback from camera
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3 , 5)

        #If a face is detected make a square around it
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0),2)

            #If found announce and then wait a few seconds before announcing again
            if(found == 1):
                print("Found Chair")
                sayWord("Watch out! There is a person up ahead!",1)
                found = 0
            time.sleep(1)

        #Display frame captured by the camera
        cv2.imshow('frame',frame)
        #This waitkey is to turn of the camera on user input of q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sayWord("Turning off App.",1)
            break

#Else response was no this means user wants to add to the database
elif response == 'n':
    sayWord("You are about to add a new object, to the database.",0)
    #Prepare Camera for object snap
    cam_port = 0
    #Prepare camera object
    cam = cv2.VideoCapture(cam_port)
    
    #Initialize voice recognizer
    r = sr.Recognizer()
    
    #for debugging
    #while(True):

    result, image = cam.read()

    #for debugging
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('image',image)
        #faces = face_cascade.detectMultiScale(gray, 1.3 , 5)
    #for debugging
        #for(x,y,w,h) in faces:
            #cv2.rectangle(image,(x,y),(x+w, y+h), (255,0,0),2)
    cv2.imshow('image',image)
    if result:
            try:
                #Speech to text to create image jpg
                sayWord("What is the name of the object?",0)
                sayWord("Please say the name.",0)
                
                #Turn on microphone
                with sr.Microphone() as source2:
                    #Adjustments for ambient noise and then listen for speech
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    audio = r.listen(source2)
                    
                    #Use Google library of speech to text
                    obj = r.recognize_google(audio)
                    obj = obj.lower()#lowercase text

                    print("Text to speech ", obj)#for back end debugging
                    #Speech to text creates file to folder
                    SpeakText(obj)
                    filename = obj + ".jpg"
                    print(filename)
                
                    sayWord("Hold the camera steady, infront of you.",1)
                    #time.sleep(3)
                    cv2.imshow(filename, image)
                
                    sayWord("Taking picture in 3, 2, 1.",1)
                
                    cv2.imwrite(filename, image)
                
                    sayWord("Press q to exit.",0)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows#close program
                   # break
            except sr.RequestError as e:
                sayWord("Could not request result; {0}")
                print("Could not request results; {0}".format(e))
            except sr.UnknownValueError:
                print("unknown error occurred")

cap.release()#Release camera
cv2.destroyAllWindows()#close program