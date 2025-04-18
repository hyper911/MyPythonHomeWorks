"""Розширити проект з грою 2048, добавити іншу палітру, добавити меню"""

import random
from ctypes import windll
from itertools import count
from math import trunc
from tkinter import *

SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#4f5752"
BACKGROUND_COLOR_CELL_EMPTY = "#a19487"

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e"}

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2",
                   16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2",
                   128: "#f9f6f2", 256: "#f9f6f2", 512: "#f9f6f2",
                   1024: "#f9f6f2", 2048: "#f9f6f2"}

FONT = ("Verdana", 40, "bold")

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"

mainframe = Frame()
grid_cell = []
matrix = []
menu = Menu(mainframe.master)
game_menu = Menu(menu, tearoff=0)
game_menu.add_command(label="New Game", command=lambda: start_game())
game_menu.add_command(label="Change palette", command=lambda: change_palette())
game_menu.add_command(label="Exit", command=lambda: quit())
menu.add_cascade(label="Game", menu=game_menu)
menu.add_command(label="About", command=lambda: windll.user32.MessageBoxW(0,
                                                                          "Game 2048\n\nAuthor: Oleksii Kachan\n\nVersion: 1.1",
                                                                          "About",
                                                                          0x00001000))


def change_palette():
    global BACKGROUND_COLOR_GAME, BACKGROUND_COLOR_CELL_EMPTY, BACKGROUND_COLOR_DICT, CELL_COLOR_DICT

    BACKGROUND_COLOR_GAME = "#99d1d1"
    BACKGROUND_COLOR_CELL_EMPTY = "#b7bfb6"

    BACKGROUND_COLOR_DICT = {2: "#90ada5", 4: "#9dd1c2", 8: "#62e3be",
                             16: "#87dfff", 32: "#62c4b1", 64: "#3369ff",
                             128: "#23367d", 256: "#5833ff", 512: "#7926ff",
                             1024: "#a526ff", 2048: "#ff2626"}

    CELL_COLOR_DICT = {2: "#474a47", 4: "#474a47", 8: "#fffff7",
                       16: "#fffff7", 32: "#fffff7", 64: "#fffff7",
                       128: "#fffff7", 256: "#fffff7", 512: "#fffff7",
                       1024: "#fffff7", 2048: "#fffff7"}

    update_grid_cell()


def init_grid():
    backgraound = Frame(bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
    backgraound.grid()

    for i in range(GRID_LEN):
        grid_row = []
        for j in range(GRID_LEN):
            cell = Frame(backgraound, bg=BACKGROUND_COLOR_CELL_EMPTY,
                         width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
            cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
            t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY,
                      justify=CENTER, font=FONT, width=5, height=2)
            t.grid()
            grid_row.append(t)
        grid_cell.append(grid_row)


def game_state():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2048:
                return "win"

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return "not over"

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == matrix[i + 1][j] or matrix[i][j] == matrix[i][
                j + 1]:
                return "not over"

    for k in range(len(matrix) - 1):
        if matrix[len(matrix) - 1][k] == matrix[len(matrix) - 1][k + 1]:
            return "not over"

    for j in range(len(matrix) - 1):
        if matrix[j][len(matrix) - 1] == matrix[j + 1][len(matrix) - 1]:
            return "not over"

    return "lose"


def add_two():
    a = random.randint(0, len(matrix) - 1)
    b = random.randint(0, len(matrix) - 1)
    while (matrix[a][b] != 0):
        a = random.randint(0, len(matrix) - 1)
        b = random.randint(0, len(matrix) - 1)
    matrix[a][b] = 2


def init_matrix():
    for i in range(GRID_LEN):
        matrix.append([0] * GRID_LEN)
    add_two()
    add_two()


def update_grid_cell():
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            if matrix[i][j] == 0:
                grid_cell[i][j].configure(text="",
                                          bg=BACKGROUND_COLOR_CELL_EMPTY)
            else:
                grid_cell[i][j].configure(text=str(matrix[i][j]),
                                          bg=BACKGROUND_COLOR_DICT[
                                              matrix[i][j]],
                                          fg=CELL_COLOR_DICT[matrix[i][j]])


def cover_up(mat):
    new = []
    for i in range(len(mat)):
        new.append([0] * len(mat))
    done = False
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat)):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return (new, done)


def merge(mat):
    done = False
    for i in range(len(mat)):
        for j in range(len(mat) - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    return (mat, done)


def left():
    global matrix
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    return done


def right():
    global matrix
    matrix = reverse(matrix)
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = reverse(matrix)
    return done


def up():
    global matrix
    matrix = transpose(matrix)
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = transpose(matrix)
    return done


def down():
    global matrix
    matrix = reverse(transpose(matrix))
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = transpose(reverse(matrix))
    return done


def reverse(mat):
    # ПОтірбно відзеркалити матрицю по горизонталі
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat) - j - 1])
    return new


def transpose(mat):
    # Поміняти стовпці і рядки місцями технічно i треба змінити в циклі на j
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new


def key_down(event):
    key = repr(event.char)
    if key in mainframe.commands:
        done = mainframe.commands[repr(event.char)]()
        if done:
            add_two()
            update_grid_cell()
            if game_state() == "win":
                grid_cell[GRID_LEN // 2 - 1][GRID_LEN // 2 - 1].configure(
                    text="You", bg=BACKGROUND_COLOR_CELL_EMPTY)
                grid_cell[GRID_LEN // 2 - 1][GRID_LEN // 2].configure(
                    text="Win", bg=BACKGROUND_COLOR_CELL_EMPTY)
            if game_state() == "lose":
                grid_cell[GRID_LEN // 2 - 1][GRID_LEN // 2 - 1].configure(
                    text="You", bg=BACKGROUND_COLOR_CELL_EMPTY)
                grid_cell[GRID_LEN // 2 - 1][GRID_LEN // 2].configure(
                    text="Lose", bg=BACKGROUND_COLOR_CELL_EMPTY)


def main():
    mainframe.master.title("2048")
    mainframe.master.bind("<Key>", key_down)
    mainframe.commands = {KEY_UP: up, KEY_DOWN: down, KEY_LEFT: left,
                          KEY_RIGHT: right}
    mainframe.master.config(menu=menu)

    init_grid()
    init_matrix()
    update_grid_cell()
    mainloop()


def start_game():
    global matrix
    matrix = []
    for i in range(GRID_LEN):
        matrix.append([0] * GRID_LEN)
    add_two()
    add_two()
    update_grid_cell()


if __name__ == "__main__":
    main()
