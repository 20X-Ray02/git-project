from tkinter import Tk, Canvas, Frame, BOTH
import math


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("График функции")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(0, 0, 1200, 1200, fill='white')

        #График функции y = sin x and y = x^2
        canvas.create_line(0, 300, 1200, 300, fill='black', width=2)
        canvas.create_line(500, 10, 500, 600, fill='black', width=2)

        center = 300
        x_increment = 1
        x_factor = 0.045
        y_amplitude = 100

        xy = []
        for x in range(980):
            xy.append((x + 10) * x_increment)
            xy.append(int(math.sin(x * x_factor) * y_amplitude) + center)

        sin_line = canvas.create_line(xy, fill='black', width=2)


        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    Example()
    root.geometry("400x250+10+20")
    root.minsize(1000, 550)
    root.maxsize(1000, 550)
    root.resizable(False, False)

    root.mainloop()


if __name__ == '__main__':
    main()
