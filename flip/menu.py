from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# custom .kv file
Builder.load_file("menu.kv");

class MyLayout(Widget):
  pass

class MenuScreenApp(App):
  def build(self):
    return MyLayout()
  
if __name__ == '__main__':
  MenuScreenApp().run()