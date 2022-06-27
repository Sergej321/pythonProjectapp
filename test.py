from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window
#from kivy.uix.floatlayout import FloatLayout


# Designate Our .kv design file
Builder.load_file('test.kv')

class MyLayout(TabbedPanel):
	pass

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()