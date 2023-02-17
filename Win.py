from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import próby


class Win(FloatLayout):
    pass


class WinApp(App):

    def build(self):
        return Win()


if __name__ == '__main__':
    WinApp().run()
