import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.textinput import TestInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

#class MyGridLayout(GridLayout)		#This would be used with the KV file if we wanted to use it
#	pass							#however with the scope of the project its not needed.

class ButtonApp(App):				#Main class this is all the logic needed to run the button
									#For simple design I included the font and label here instead of kv file
#	name = ObjectProperty(None)
#	color = ObjectProperty(None)

	def build(self):
		btn = Button(text ="Start", font_size="160sp")
		return btn
root = ButtonApp()
root.run()

#class RootWidget(BoxLayout):		#This is a widget method I added. We can use this to toggle the button text  
#	def btn_clk(self):				#when pressed.
#		self.label.text = "ON"

#class ActionApp(App):				#Alternative method we could use.
#	def build(self):
#		return RootWidget()
#MyApp = ActionApp()
#MyApp.run()

# class MyApp(App):					#This was a test method I added in the beginning.
#	def build(self):
#		return Label(test="Start")

# if __name__ == '__main__':
#	ButtonApp().run()