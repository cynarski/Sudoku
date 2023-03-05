from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('loss.kv', rulesonly=True)


class Loss(Screen):

    def new_game_button_click(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'screen_one'

    def exit_button_click(self):
        App.get_running_app().stop()

