#Title: Kivy App
#Authors: Manuel Holguin, Derek Oda, Seth Ball, Gabe Romero
#Date: 12-05-2022
#Description: Kivy application project which will run
#       object recognition on mobile devices. With the 
#       intention of helping the visually impaired individuals
#       includes a .kv files that works as a CSS file managing
#       all the front end visual aspects of the App.
#

#App dependecies
from kivy.app import App # Main Application
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition #Screen Pagination
from kivy.uix.boxlayout import BoxLayout # Layout format for Kivy
from kivy.lang import Builder # Used to import the .kv file
from kivy.uix.button import Button #Import for kivy buttons
from kivy.core.audio import SoundLoader #Android import for audio feedback
from kivy.uix.widget import Widget # kivy widget for app configurations Building blocks
#from plyer import tts, vibrator #For android virbration feedback
import time
#import cv2 #Computer Vision library
#import pyttsx3 #Import for Audio feedback on python

#The classes(Screen) represent the pagination system for the app
#   to create another page in the app for example to display configurations
#   you would create another class called 
#   Configurations(Screen)
class MainMenu(Screen):
    pass# If there is nothing to implement in the page
        # just insert a pass 

#Navigation Page
class Navigation(Screen):
    #This section was intended to implement object recognition in Kivy
    #Has multiple deep errors need further testing.
    """
    def objectRec(self):
        def sayWord(word,num):
            print(word)
    # Initialize the engine
            engine = pyttsx3.init()
            engine.say(word)
            engine.runAndWait()
            time.sleep(num)

        cap = self.ids['cameratwo']
        #cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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
    """
    pass

#Camera page handles the camera feature in the App
#Also includes the functions that are run by the .kv file
class CameraScreen(Screen):
    
    #Function passes self (instance) and widget(Object defined or Passed)
    def pressed(self, widget):
        
        #The camera object has a state function which determines if
        # the camera is on or off in the next statements the state
        # is used to change the text of the toggleButton
        #Widget(Camera).state
        if widget.state == "normal":
            widget.text = "START"

        else:
            widget.text = "OFF"   

    #When the user presses the capture button in the App
    #   the function is called which takes a snap and saves it
    #   to the directory.
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        #In kivy much like in HTML we have id that helps pass the object
        #   here we are saying get the object with id camera
        #   and set it to camera
        camera = self.ids['camera']
        #get timestamp
        timestr = time.strftime("%Y%m%d_%H%M%S")
        #Then the camera object export the png 
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured") 
    pass

#This is the main class that runs the App anything that needs to
#   operate in the global aspect is inserted here.
class Main(App):
    #user Builder to load .kv file
    #   and also create the pages
    def build(self):
        Builder.load_file("obkiv.kv")

        #sm is the name of the object and ScreenManager is a 
        #   attribute of screenmanager that is used for pagination
        #   all I am doing here is setting up a transition for the pages
        sm = ScreenManager(transition = FadeTransition())
        #Creating pages with a name attribute for identification
        sm.add_widget(MainMenu(name= "main"))
        sm.add_widget(Navigation(name="navigation"))
        sm.add_widget(CameraScreen(name="camera"))

        return sm

    #Used for audio feedback but was not fully implemented in the App        
    def init_audio(self):
        self.sound_begin = SoundLoader.load()

    #def loading(self, text_to_speak):
     #   tts.speak(text_to_speak)

    #def vibrate(self):
     #   vibrator.vibrate(time=1.5)

#Run Main App
if __name__ == '__main__':
    
    Main().run()
