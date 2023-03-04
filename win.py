from kivy.app import App
from kivy.uix.screenmanager import Screen


class Win(Screen):
    def update_timer(self, game_time):
        minutes, seconds = game_time
        self.time_label.text = "%d:%02d" % (minutes, seconds)

    def new_game_button_click(self):
        self.manager.current = 'screen_one'

    def exit_button_click(self):
        App.get_running_app().stop()



