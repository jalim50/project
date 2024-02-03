import kivy
from kivy.app import App 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager , Screen
Window.size=(400,630)
Window.clearcolor=(0,0,0,0)


class Window1(Screen):
    pass
class Window2(Screen):
    pass
class WindowManager(ScreenManager):
    pass


kv=Builder.load_file('dsineEx2.kv')
class Myapp(App):
    def build(self):
        self.title=('jalim app')
        return kv
        

Myapp().run()