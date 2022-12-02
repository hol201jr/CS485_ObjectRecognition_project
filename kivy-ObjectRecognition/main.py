from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.camera import Camera
import time

#content layouts examples
#1st example box layouts usage in Python
#can be useful if you need to make loops in python for
#multiple boxes
class BoxLayoutExample(BoxLayout):
    pass
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="Navigate")
        b2 = Button(text="Camera")
        b3 = Button(text="exit")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """
    #Create the camera Object
    def capture(self):
        layout = BoxLayout(orientation = 'vertical')

        self.cameraObject.index = 0
        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (300 , 300)

        # Create a button for taking photograph

        self.camaraClick = Button(text="Take Photo")

        self.camaraClick.size_hint=(.5, .2)

        self.camaraClick.pos_hint={'x': .25, 'y':.75}

        # bind the button's on_press to onCameraClick

        self.camaraClick.bind(on_press = self.onCameraClick())

       

        # add camera and button to the layout

        layout.add_widget(self.cameraObject)

        layout.add_widget(self.camaraClick)

       

        # return the root widget

        return layout

# Take the current frame of the video as the photo graph       

def onCameraClick(self, **kwargs):

        self.cameraObject.export_to_png('/kivyexamples/selfie.png')

class AnchorLayoutExample(AnchorLayout):
    pass
#main interface
class MainWidget(Widget):
    pass

#camera class
class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

class TheLabApp(App):
    pass

TheLabApp().run()