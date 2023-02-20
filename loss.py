from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import start

Builder.load_file('losskivy.kv', rulesonly=True)

class Loss(FloatLayout):

    def new_game_button_click(self):
        App.get_running_app().stop()
        start.StartApp().run()

    def exit_button_click(self):
        App.get_running_app().stop()


class LossApp(App):

    def build(self):
        return Loss()


