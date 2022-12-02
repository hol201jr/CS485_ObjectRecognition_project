from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button

class MainMenu(Screen):
    pass

class Navigation(Screen):
    pass

class CameraScreen(Screen):
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
