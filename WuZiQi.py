import tkinter as tk
from NativeAPI import EnableHighDPISupport, GetScreenResolution
import json
from JSock import JSock

# Preferences
highDPI = True


def CreateWindow(width, height, title):
    root = tk.Tk()
    root.geometry(str(width) + "x" + str(height))
    root.title(title)
    return root


def CreateCanvas(root, x, y, width, height):
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.place(x=x, y=y)
    return canvas


def CreateCircle(canvas, x, y, width, color):
    tkOffsetBugfix = int(0.13 * width)
    canvas.create_oval(
        x + tkOffsetBugfix,
        y + tkOffsetBugfix,
        x + tkOffsetBugfix + width,
        y + tkOffsetBugfix + width,
        fill=color, outline=color
    )


def CreatePiece(canvas, i, j, halfGridSize, color):
    y = i
    x = j
    CreateCircle(canvas, x * 2 * halfGridSize, y * 2 * halfGridSize, int(0.85 * halfGridSize * 2), color)


def MouseClickCallback(event):
    mx, my = event.x, event.y

    i = my // (2 * halfGridSize)
    j = mx // (2 * halfGridSize)
    print(i, j)

    CreatePiece(canvas, i, j, halfGridSize, color="black")


root = None
jsock = None


def IntervalFunction():

    # Close or Not
    jsock.SendStr("CloseOrNot")
    result = jsock.RecvStr()
    if result == "Yes":
        root.destroy()

    root.after(1, IntervalFunction)


if __name__ == "__main__":
    if highDPI:
        EnableHighDPISupport()

    screenResolution = GetScreenResolution()
    print(screenResolution)

    if highDPI:
        halfGridSize = int(0.03 * screenResolution[1])
    else:
        halfGridSize = 15
    print(halfGridSize)

    width = 9
    height = 9
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

    canvas.bind("<Button-1>", MouseClickCallback)

    # Set Network Socket Interval
    jsock = JSock()
    jsock.Connect("127.0.0.1", 16521)
    root.after(1, IntervalFunction)

    root.mainloop()
