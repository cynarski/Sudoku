from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import start

Builder.load_file('losskivy.kv', rulesonly=True)


class Loss(Screen):

    def new_game_button_click(self):
        self.manager.current = 'screen_one'

    def exit_button_click(self):
        App.get_running_app().stop()


class LossApp(App):

    def build(self):
        return Loss()


