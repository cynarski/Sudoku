import random

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from sudoku import Sudoku

levels = ["EASY", "MEDIUM", "HARD"]


class SudokuBoard(GridLayout, Screen):
    time_elapsed = NumericProperty(0)

    def __init__(self, puzzle, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 5
        self.spacing = 5
        self.padding = 5
        self.puzzle_to_function = puzzle
        self.lives = 3
        self.start_time = None
        self.clock_event = Clock.schedule_interval(self.update_time, 0.1)
        self.finsh_time = 0
        self.level = "xd"
        self.next_game = False

        self.board = [[TextInput(input_filter='int', multiline=False, halign='center', font_size=30) for _ in range(9)]
                      for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.board[i][j].text = str(puzzle[i][j])
                self.board[i][j].readonly = True
                self.board[i][j].foreground_color = (0, 0, 0, 1)
                self.board[i][j].bind(text=self.check_number)
                self.board[i][j].id = f"{i}-{j}"
                self.board[i][j].bind(on_touch_down=self.activate_text_input)

        # Create 9 smaller squares
        self.create_board()
        # lives and time of the game
        self.box_lives = self.lives_display()
        self.add_widget(self.box_lives)

        self.level_label = Label(text=self.level, font_size=30)
        self.add_widget(self.level_label)

        self.label = Label(text="0:00", font_size=30)
        self.add_widget(self.label)
        # new game - button
        self.add_widget(self.new_game_button())
        self.add_widget(Label(text="     Created by:\n Michał Cynarski\n Mateusz Cierpik",font_size=25))
        self.add_widget(self.exit_button())

    def create_small_square(self, row, col):
        small_square = BoxLayout(orientation='vertical', size_hint=(1, 1))
        for i in range(3):
            row_box = BoxLayout(orientation='horizontal', size_hint=(1, 1))
            for j in range(3):
                row_box.add_widget(self.board[row + i][col + j])
            small_square.add_widget(row_box)
        return small_square

    def create_board(self):
        self.clear_widgets()
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                self.add_widget(self.create_small_square(i, j))

    def lives_display(self):
        label1 = Label(text="3/3", font_size=40, color=(1, 0, 0, 1))
        return label1

    def new_game_button(self):
        layout = BoxLayout(orientation='vertical')
        new_game_button = Button(text="New Game", font_size=30, color=(1, 0, 0, 1))
        new_game_button.bind(on_press=self.new_game)
        layout.add_widget(new_game_button)
        return layout

    def exit_button(self):
        layout = BoxLayout(orientation='vertical')
        exit_button = Button(text="Exit", font_size=30, color=(1, 0, 0, 1))
        exit_button.bind(on_press=self.exit)
        layout.add_widget(exit_button)
        return layout

    def add_level(self, instance):
        label = Label(text=self.level, font_size=30)
        return label

    def update_level_label(self, level):
        self.level = level
        self.level_label.text = self.level

    def update_time(self, dt):
        if not self.start_time:
            self.start_time = Clock.get_time()
        self.time_elapsed = Clock.get_time() - self.start_time
        minutes = int(self.time_elapsed / 60)
        seconds = int(self.time_elapsed % 60)
        self.label.text = " %d:%02d" % (minutes, seconds)

    def end_time(self):
        self.clock_event.cancel()
        minutes = int(self.time_elapsed / 60)
        seconds = int(self.time_elapsed % 60)
        self.finsh_time = (minutes,seconds)

    def activate_text_input(self, instance, touch):
        # called when the text input field is touched
        if instance.collide_point(*touch.pos):
            instance.focus = True

    def remove_random_cells(self, count):
        removed_cells = []
        while len(removed_cells) < count:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            cell = (row, col)
            if cell not in removed_cells:
                self.board[row][col].text = ""
                self.board[row][col].readonly = False
                removed_cells.append(cell)

    def new_game(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'screen_one'

    def exit(self, instance):
        App.get_running_app().stop()

    def on_pre_enter(self):
        #if not self.manager.get_screen('screen_two').children:
        if self.next_game:
            self.create_board_object()

    def create_board_object(self):
        sudoku = Sudoku(random.choice(levels))
        puzzle = sudoku.solve()

        screen_manager = self.manager
        screen_manager.remove_widget(self)
        screen_two = SudokuBoard(name='screen_two', puzzle=puzzle)
        screen_manager.add_widget(screen_two)
        screen_manager.current = 'screen_two'

    def on_leave(self):
        #self.manager.remove_widget(self)
        #self.clear_widgets()
        self.next_game = True

    def check_number(self, instance, value):
        row, col = instance.id.split("-")
        row = int(row)
        col = int(col)
        number = instance.text

        self.board[row][col].background_color = (1, 1, 1, 1)
        if number:
            if self.puzzle_to_function[row][col] != number:
                self.board[row][col].background_color = (1, 0, 0, 0.7)
                self.lives -= 1
                self.box_lives.text = str(self.lives) + "/3"
                if self.lives <= 0:
                    self.manager.transition.direction = 'left'
                    self.manager.current = 'screen_three'
            else:
                self.board[row][col].readonly = True
                number_box_empty = False
                for i in range(9):
                    for j in range(9):
                        if self.board[i][j].text == "":
                            number_box_empty = True

                if not number_box_empty:
                    minutes = int(self.time_elapsed / 60)
                    seconds = int(self.time_elapsed % 60)
                    game_time = minutes, seconds
                    self.manager.transition.direction = 'left'
                    self.manager.current = 'screen_four'
                    screen_four = self.manager.get_screen('screen_four')
                    screen_four.update_timer(game_time)

        else:
            instance.text = ''


class SudokuApp(App):
    def __init__(self, counter=0, level="", **kwargs):
        super().__init__(**kwargs)
        self.counter = counter
        self.level = level

    def build(self):
        sudoku = Sudoku(random.choice(levels))
        puzzle = sudoku.solve()
        sudoku_to_play = SudokuBoard(puzzle)
        sudoku_to_play.remove_random_cells(self.counter)
        sudoku_to_play.add_level(self.level)
        return sudoku_to_play
