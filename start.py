from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy import Config
import random
import proby

Builder.load_file('startkivy.kv', rulesonly=True)


class Start(FloatLayout):

    def easy_button_click(self):
        counter = random.randint(10, 20)
        print(counter)
        App.get_running_app().stop()
        level = "EASY"
        proby.SudokuApp(counter, level).run()

    def medium_button_click(self):
        counter = random.randint(21, 35)
        print(counter)
        App.get_running_app().stop()
        level = "MEDIUM"
        proby.SudokuApp(counter, level).run()

    def hard_button_click(self):
        counter = random.randint(35, 55)
        print(counter)
        App.get_running_app().stop()
        level = "HARD"
        proby.SudokuApp(counter, level).run()


class StartApp(App):

    def build(self):
        return Start()
