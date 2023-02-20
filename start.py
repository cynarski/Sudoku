from kivy import Config
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import proby
import random
from kivy.lang import Builder

Builder.load_file('startkivy.kv', rulesonly=True)

class Start(FloatLayout):


    def easy_button_click(self):
        counter = random.randint(1,2)
        print(counter)
        App.get_running_app().stop()
        proby.SudokuApp(counter).run()


    def medium_button_click(self):
        counter = random.randint(21, 35)
        print(counter)
        App.get_running_app().stop()
        proby.SudokuApp(counter).run()

    def hard_button_click(self):
        counter = random.randint(35, 55)
        print(counter)
        App.get_running_app().stop()
        proby.SudokuApp(counter).run()


class StartApp(App):

    def build(self):
        return Start()


if __name__ == '__main__':
    Config.read('configstart.ini')
    StartApp().run()
