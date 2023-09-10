import random
from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI(int(input('Введите кол-во домов: ')))

    def initUI(self, count):
        self.parent.title("House")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)


        for i in range(count):
            x = random.randint(0, 700)
            y = random.randint(0, 700)
            scl = random.randint(1, 5)
            #Крыша
            canvas.create_polygon(150 / 10 * scl + x, 195 / 10 * scl + y, 600 / 10 * scl + x, 300 / 10 * scl + y, 1140 / 10 * scl + x, 195 / 10 * scl + y, 835 / 10 * scl + x, 135 / 10 * scl + y, fill='#800000', outline='black'),
            canvas.create_polygon(150 / 10 * scl + x, 185 / 10 * scl + y, 150 / 10 * scl + x, 195 / 10 * scl + y, 835 / 10 * scl + x, 135 / 10 * scl + y, 835 / 10 * scl + x, 125 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(835 / 10 * scl + x, 135 / 10 * scl + y, 835 / 10 * scl + x, 125 / 10 * scl + y, 1140 / 10 * scl + x, 185 / 10 * scl + y, 1140 / 10 * scl + x, 195 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(150 / 10 * scl + x, 185 / 10 * scl + y, 835 / 10 * scl + x, 125 / 10 * scl + y, 675 / 10 * scl + x, 50 / 10 * scl + y, fill='#b22222', outline='black'),
            canvas.create_polygon(835 / 10 * scl + x, 125 / 10 * scl + y, 675 / 10 * scl + x, 50 / 10 * scl + y, 1140 / 10 * scl + x, 185 / 10 * scl + y, fill='#b22222', outline='black'),
            #Стены
            canvas.create_polygon(200 / 10 * scl + x, 200 / 10 * scl + y, 200 / 10 * scl + x, 500 / 10 * scl + y, 800 / 10 * scl + x, 600 / 10 * scl + y, 800 / 10 * scl + x, 150 / 10 * scl + y, fill='#e0e094', outline='black'),
            canvas.create_polygon(800 / 10 * scl + x, 150 / 10 * scl + y, 800 / 10 * scl + x, 600 / 10 * scl + y, 1100 / 10 * scl + x, 475 / 10 * scl + y, 1100 / 10 * scl + x, 200 / 10 * scl + y, fill='#e0e094', outline='black'),
            #Дополнительные элементы
            canvas.create_polygon(200 / 10 * scl + x, 200 / 10 * scl + y, 200 / 10 * scl + x, 210 / 10 * scl + y, 800 / 10 * scl + x, 160 / 10 * scl + y, 800 / 10 * scl + x, 150 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(800 / 10 * scl + x, 150 / 10 * scl + y, 800 / 10 * scl + x, 160 / 10 * scl + y, 1100 / 10 * scl + x, 206 / 10 * scl + y, 1100 / 10 * scl + x, 200 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(200 / 10 * scl + x, 320 / 10 * scl + y, 200 / 10 * scl + x, 350 / 10 * scl + y, 800 / 10 * scl + x, 375 / 10 * scl + y, 800 / 10 * scl + x, 345 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(800 / 10 * scl + x, 345 / 10 * scl + y, 800 / 10 * scl + x, 374 / 10 * scl + y, 1100 / 10 * scl + x, 340 / 10 * scl + y, 1100 / 10 * scl + x, 322 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(200 / 10 * scl + x, 480 / 10 * scl + y, 200 / 10 * scl + x, 500 / 10 * scl + y, 800 / 10 * scl + x, 600 / 10 * scl + y, 800 / 10 * scl + x, 580 / 10 * scl + y,fill='#c1bba4', outline='black'),
            canvas.create_polygon(200 / 10 * scl + x, 490 / 10 * scl + y, 200 / 10 * scl + x, 500 / 10 * scl + y, 800 / 10 * scl + x, 600 / 10 * scl + y, 800 / 10 * scl + x, 590 / 10 * scl + y, fill='#c1bba4', outline='black'),
            canvas.create_polygon(800 / 10 * scl + x, 580 / 10 * scl + y, 800 / 10 * scl + x, 600 / 10 * scl + y, 1100 / 10 * scl + x, 475 / 10 * scl + y, 1100 / 10 * scl + x, 460 / 10 * scl + y,fill='#c1bba4', outline='black'),
            canvas.create_polygon(800 / 10 * scl + x, 590 / 10 * scl + y, 800 / 10 * scl + x, 600 / 10 * scl + y, 1100 / 10 * scl + x, 475 / 10 * scl + y, 1100 / 10 * scl + x, 468 / 10 * scl + y, fill='#c1bba4', outline='black'),
            #Дверь
            canvas.create_polygon(295 / 10 * scl + x, 355 / 10 * scl + y, 295 / 10 * scl + x, 496 / 10 * scl + y, 350 / 10 * scl + x, 505 / 10 * scl + y, 350 / 10 * scl + x, 357 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(300 / 10 * scl + x, 355 / 10 * scl + y, 300 / 10 * scl + x, 495 / 10 * scl + y, 350 / 10 * scl + x, 505 / 10 * scl + y, 350 / 10 * scl + x, 357 / 10 * scl + y, fill='#1d3ec2', outline='black', width='3'),

        canvas.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    root.geometry("1000x1000")
    app = Example(root)
    root.minsize(1240, 700)
    root.resizable(True, True)

    root.mainloop()

main()
