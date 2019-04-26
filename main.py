from kivy.app import App
from kivy.uix.button import Button


class Ball:
    color: str

    def move(self):
        pass

    def push(self):
        pass

    def take(self):
        pass

class TestApp(App):
    def build(self):
        return Button(text='Hello World')


TestApp().run()
