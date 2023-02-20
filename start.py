from kivy import Config
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from proby import SudokuBoard,SudokuApp
import random


class Start(FloatLayout):


    def easy_button_click(self):
        counter = random.randint(10,20)
        print(counter)
        App.get_running_app().stop()
        SudokuApp(counter).run()
        StartApp().run()


    def medium_button_click(self):
        counter = random.randint(21, 35)
        print(counter)
        App.get_running_app().stop()
        SudokuApp(counter).run()
        StartApp().run()

    def hard_button_click(self):
        counter = random.randint(35, 55)
        print(counter)
        App.get_running_app().stop()
        SudokuApp(counter).run()
        StartApp().run()


class StartApp(App):

    def build(self):
        return Start()


if __name__ == '__main__':
    Config.read('configstart.ini')
    StartApp().run()
