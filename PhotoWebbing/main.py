from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

import os


Builder.load_file(os.path.dirname(__file__)+ 'PhotoWebbing.kv')


class MainWindow(BoxLayout):
    pass


class PhotoWebbing(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    PhotoWebbing().run()
