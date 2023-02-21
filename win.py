from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import start

Builder.load_file('winkivy.kv', rulesonly=True)


class Win(FloatLayout):
    def __init__(self, game_time, **kwargs):
        super().__init__(**kwargs)
        self.minutes, self.seconds = game_time
        self.time_label.text = "%d:%02d" % (self.minutes, self.seconds)

    def new_game_button_click(self):
        App.get_running_app().stop()
        print("Twój czas wynosi: %d:%02d" % (self.minutes, self.seconds))
        start.StartApp().run()

    def exit_button_click(self):
        print("Twój czas wynosi: %d:%02d" % (self.minutes, self.seconds))
        App.get_running_app().stop()

    def time_to_text(self,iterations):
        return "%d:%02d" % (self.minutes, self.seconds)



class WinApp(App):
    def __init__(self, game_time, **kwargs):
        super().__init__(**kwargs)
        self.game_time = game_time

    def build(self):
        return Win(self.game_time)


