from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from dokusan import generators,renderers,solvers
import random
from sudoku import Sudoku

levels = ["EASY", "MEDIUM", "HARD"]


class SudokuBoard(GridLayout):
    def __init__(self, puzzle, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 4
        self.spacing = 5
        self.padding = 5
        self.puzzle_to_function = puzzle
        self.lives = 3
        self.heart = '\u2665'

        # Stwórz 9x9 siatkę pól tekstowych
        self.board = [[TextInput(input_filter='int', multiline=False, halign='center', font_size=30) for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.board[i][j].text = str(puzzle[i][j])
                self.board[i][j].readonly = False
                self.board[i][j].foreground_color = (0, 0, 0, 1)
                self.board[i][j].bind(text=self.check_number)
                self.board[i][j].id = f"{i}-{j}"

        # Stwórz 9 mniejszych kwadratów
        self.create_board()
        self.remove_random_cells(20)
        # życia i czas gry
        self.box_lives = self.lives_display()
        self.add_widget(self.box_lives)
        # nowa gra - przycisk
        self.add_widget(self.new_game_button())

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
        hearts = self.heart * self.lives
        label1 = Label(text=hearts, font_name="Arial", font_size=40, color=(1, 0, 0, 1))
        return label1

    def new_game_button(self):
        layout = BoxLayout(orientation='vertical')
        new_game_button = Button(text="Nowa Gra", font_name="Arial", font_size=30, color=(1, 0, 0, 1))
        new_game_button.bind(on_press=self.new_game)
        layout.add_widget(new_game_button)
        return layout

    def remove_random_cells(self,count):
        for i in range(count):
            row = random.randint(0,8)
            col = random.randint(0,8)
            self.board[row][col].text = ""

    def new_game(self, instance):
        App.get_running_app().stop()
        SudokuApp().run()

    def check_number(self, instance, value):
        # Pobierz indeksy wiersza i kolumny z atrybutu id
        row, col = instance.id.split("-")
        row = int(row)
        col = int(col)

        # Pobierz wprowadzoną liczbę
        number = instance.text

        self.board[row][col].background_color = (1, 1, 1, 1)
        # Sprawdź, czy liczba jest poprawna
        if number:
            # Liczba jest podana - sprawdź, czy jest prawidłowa
            if self.puzzle_to_function[row][col] != number:
                # Liczba jest nieprawidłowa - wyświetl komunikat błędu
                self.board[row][col].background_color = (1, 0, 0, 0.7)
                self.lives -= 1
                hearts = self.heart * self.lives
                self.box_lives.text = hearts
                if self.lives <= 0:
                    self.box_lives.text = "PORAŻKA :("
                    # zablokowanie wpisywania po przegranej
                    for i in range(9):
                        for j in range(9):
                            self.board[i][j].readonly = True
        else:
            # Liczba nie j
            instance.text = ''


class SudokuApp(App):
    def build(self):
        # tutaj wstawiasz swoje puzzle Sudoku jako tablicę 9x9
        sudoku = Sudoku(random.choice(levels))
        puzzle = sudoku.solve()
        return SudokuBoard(puzzle)


if __name__ == '__main__':
    SudokuApp().run()
