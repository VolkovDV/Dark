from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from plyer import accelerometer
from kivy.clock import Clock


class Ball(Widget):
    color: str = 'ddd'
    _disabled_count: int = 0


    def __init__(self):
        super(Ball, self).__init__()

    def show(self):
        return Image(source='Anonymous_Life_Saver.png')

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
        p = Ball()
        return p.show()


TestApp().run()
