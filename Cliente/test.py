import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

from kivymd.uix.boxlayout import MDBoxLayout

class MyWidget(MDBoxLayout):
    pass

class BasicApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return MyWidget()

if __name__ == '__main__':
    Window.size = (800, 600)
    Window.fullscreen = False
    BasicApp().run()