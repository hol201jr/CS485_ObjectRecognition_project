from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from plyer import tts, vibrator
import time

class MainMenu(Screen):
    pass

class Navigation(Screen):
    pass

class CameraScreen(Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
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
    def init_audio(self):
        self.sound_begin = SoundLoader.load()

    def loading(self, text_to_speak):
        tts.speak(text_to_speak)

    def vibrate(self):
        vibrator.vibrate(time=1.5)

       

if __name__ == '__main__':
    
    Main().run()
