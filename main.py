from kivy.app import App
from kivy.uix.button import Button


class Ball:
    color: str

    def __init__(self):
        pass

    def move(self):
        pass

    def push(self):
        pass

    def take(self):
        pass

    @property
    def health(self):
        pass



class TestApp(App):
    def build(self):
        return Button(text='Hello World')


TestApp().run()
