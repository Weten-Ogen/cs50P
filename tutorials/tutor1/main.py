from cgitb import text
from kivy.app import App, Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutExpl(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b2)
    #     self.add_widget(b1)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass

class ChasorApp(App):
    def build(self):
        return Builder.load_file('Chasor.kv')


ChasorApp().run()