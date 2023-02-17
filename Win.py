from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import próby


class Win(FloatLayout):

    def new_game_button_click(self):
        pass

    def exit_button_click(self):
        App.get_running_app().stop()


class WinApp(App):

    def build(self):
        return Win()


if __name__ == '__main__':
    WinApp().run()
