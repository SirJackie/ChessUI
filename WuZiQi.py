import tkinter as tk
from tkinter import PhotoImage


def CreateWindow(width, height, title):
    root = tk.Tk()
    root.geometry(str(width) + "x" + str(height))
    root.title(title)
    return root


def CreateCanvas(root, x, y, width, height):
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.place(x=x, y=y)
    return canvas


def CreateCircle(canvas, x, y, color):
    canvas.create_oval(x + 2, y + 2, x + 28, y + 28, fill=color, outline=color)


def CreatePiece(canvas, i, j, halfGridSize, color):
    y = i
    x = j
    CreateCircle(canvas, x * 2 * halfGridSize, y * 2 * halfGridSize, color)


width = 9
height = 9
halfGridSize = 15
winWidth = width * 2 * halfGridSize
winHeight = height * 2 * halfGridSize

root = CreateWindow(winWidth, winHeight, "ChessUI")
canvas = CreateCanvas(root, 0, 0, winWidth, winHeight)

# Horizontal
for dy in range(0, height):
    x1 = halfGridSize
    y1 = halfGridSize + dy * 2 * halfGridSize
    x2 = halfGridSize + (width - 1) * 2 * halfGridSize
    y2 = halfGridSize + dy * 2 * halfGridSize
    canvas.create_line(x1, y1, x2, y2)

# Vertical
for dx in range(0, width):
    x1 = halfGridSize + dx * 2 * halfGridSize
    y1 = halfGridSize
    x2 = halfGridSize + dx * 2 * halfGridSize
    y2 = halfGridSize + (height - 1) * 2 * halfGridSize
    canvas.create_line(x1, y1, x2, y2)


def play(event):
    mx, my = event.x, event.y

    i = my // (2 * halfGridSize)
    j = mx // (2 * halfGridSize)
    print(i, j)
    
    CreatePiece(canvas, i, j, halfGridSize, color="black")


canvas.bind("<Button-1>", play)


root.mainloop()
