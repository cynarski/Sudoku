from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy import Config
from kivy.uix.screenmanager import ScreenManager, Screen
import random
import proby
import loss
import win
from sudoku import Sudoku


Builder.load_file('startkivy.kv', rulesonly=True)


class Start(Screen):

    def easy_button_click(self):
        counter = random.randint(10, 20)
        level = "EASY"
        self.manager.current = 'screen_two'
        screen_two = self.manager.get_screen('screen_two')
        screen_two.remove_random_cells(counter)
        screen_two.update_level_label(level)

    def medium_button_click(self):
        counter = random.randint(21, 35)
        level = "MEDIUM"
        self.manager.current = 'screen_two'
        screen_two = self.manager.get_screen('screen_two')
        screen_two.remove_random_cells(counter)
        screen_two.update_level_label(level)

    def hard_button_click(self):
        counter = random.randint(35, 55)
        level = "HARD"
        self.manager.current = 'screen_two'
        screen_two = self.manager.get_screen('screen_two')
        screen_two.remove_random_cells(counter)
        screen_two.update_level_label(level)


class StartApp(App):

    def build(self):
        screen_manager = ScreenManager()
        screen_one = Start(name='screen_one')

        levels = ["EASY", "MEDIUM", "HARD"]
        sudoku = Sudoku(random.choice(levels))
        puzzle = sudoku.solve()

        screen_two = proby.SudokuBoard(name='screen_two', puzzle=puzzle)
        screen_three = loss.Loss(name='screen_three')
        screen_four = win.Win(name='screen_four')

        screen_manager.add_widget(screen_one)
        screen_manager.add_widget(screen_two)
        screen_manager.add_widget(screen_three)
        screen_manager.add_widget(screen_four)
        return screen_manager



