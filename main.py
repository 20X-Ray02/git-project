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
            
        canvas.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    root.geometry("1000x1000")
    app = Example(root)
    root.minsize(1240, 700)
    root.resizable(True, True)

    root.mainloop()

main()
