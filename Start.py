from kivy import Config
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from próby import SudokuBoard,SudokuApp
import random


class Start(FloatLayout):

    def easy_button_click(self):
        print("EASY")
        counter = random.randint(10,20)
        print(counter)
        SudokuBoard.remove_random_cells(self,counter)
        SudokuApp.run()


    def medium_button_click(self):
        print("MEDIUM")
        counter = random.randint(21, 35)
        print(counter)

    def hard_button_click(self):
        print("HARD")
        counter = random.randint(35, 55)
        print(counter)


class StartApp(App):

    def build(self):
        return Start()


if __name__ == '__main__':
    Config.read('configstart.ini')
    StartApp().run()
