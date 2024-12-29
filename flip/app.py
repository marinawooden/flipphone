from kivy.config import Config
Config.set('graphics', 'width', '176')
Config.set('graphics', 'height', '220')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


class HomeWindow(Screen):
  pass

class MenuWindow(Screen):
  pass

class WindowManager(ScreenManager):
  pass

# custom .kv file
Builder.load_file("app.kv")

class FlipPhoneApp(App):
  def build(self):
    sm = ScreenManager(transition=NoTransition())
    sm.add_widget(HomeWindow(name='home'))
    sm.add_widget(MenuWindow(name='menu'))

    return sm

if __name__ == '__main__':
  FlipPhoneApp().run()