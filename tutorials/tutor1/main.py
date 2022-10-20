from xml.sax import parseString
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


class ChasorApp(App):
    pass

class WidgetExample(GridLayout):
    my_text = StringProperty("Hello")
    def on_button_click(self):
        self.my_text == "who are you ? "

    
        


ChasorApp().run()