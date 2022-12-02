from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.camera import Camera
import cv2
import time

class MainMenu(Screen):
    pass

class Navigation(Screen):
    pass

class CameraScreen(Screen):
    def capture(self):
        #camera = Camera(play = True)
        #camera.index(1)
        #camera.resolution(720, 720)
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
    pass


class Main(App):
    def build(self):
        Builder.load_file("obkiv.kv")

        sm = ScreenManager(transition = FadeTransition())
        sm.add_widget(MainMenu(name= "main"))
        sm.add_widget(Navigation(name="navigation"))
        sm.add_widget(CameraScreen(name="camera"))

        return sm
        

if __name__ == '__main__':
    
    Main().run()
