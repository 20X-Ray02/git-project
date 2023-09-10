import random
from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI(int(input()))

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
            #Окна
            canvas.create_polygon(221 / 10 * scl + x, 351 / 10 * scl + y, 221 / 10 * scl + x, 403 / 10 * scl + y, 255 / 10 * scl + x, 407 / 10 * scl + y, 256 / 10 * scl + x, 353 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(225 / 10 * scl + x, 351 / 10 * scl + y, 225 / 10 * scl + x, 400 / 10 * scl + y, 255 / 10 * scl + x, 403 / 10 * scl + y, 255 / 10 * scl + x, 353 / 10 * scl + y, fill='white', outline='black', width='3'),
            canvas.create_polygon(696 / 10 * scl + x, 396 / 10 * scl + y, 696 / 10 * scl + x, 504 / 10 * scl + y, 750 / 10 * scl + x, 511 / 10 * scl + y, 751 / 10 * scl + x, 399 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(700 / 10 * scl + x, 400 / 10 * scl + y, 700 / 10 * scl + x, 500 / 10 * scl + y, 750 / 10 * scl + x, 507 / 10 * scl + y, 750 / 10 * scl + x, 403 / 10 * scl + y, fill='white', outline='black', width='3'),
            canvas.create_polygon(624 / 10 * scl + x, 391 / 10 * scl + y, 624 / 10 * scl + x, 494 / 10 * scl + y, 679 / 10 * scl + x, 501 / 10 * scl + y, 679 / 10 * scl + x, 394 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(628 / 10 * scl + x, 395 / 10 * scl + y, 628 / 10 * scl + x, 490 / 10 * scl + y, 678 / 10 * scl + x, 497 / 10 * scl + y, 678 / 10 * scl + x, 398 / 10 * scl + y, fill='white', outline='black', width='3'),
            canvas.create_polygon(246 / 10 * scl + x, 221 / 10 * scl + y, 246 / 10 * scl + x, 296 / 10 * scl + y, 310 / 10 * scl + x, 299 / 10 * scl + y, 310 / 10 * scl + x, 216 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(250 / 10 * scl + x, 225 / 10 * scl + y, 250 / 10 * scl + x, 292 / 10 * scl + y, 310 / 10 * scl + x, 295 / 10 * scl + y, 310 / 10 * scl + x, 220 / 10 * scl + y, fill='white', outline='black', width='3'),
            canvas.create_line(280 / 10 * scl + x, 223 / 10 * scl + y, 280 / 10 * scl + x, 296 / 10 * scl + y, fill='black', width='3'),
            canvas.create_polygon(631 / 10 * scl + x, 191 / 10 * scl + y, 631 / 10 * scl + x, 301 / 10 * scl + y, 720 / 10 * scl + x, 304 / 10 * scl + y, 720 / 10 * scl + x, 186 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(635 / 10 * scl + x, 195 / 10 * scl + y, 635 / 10 * scl + x, 297 / 10 * scl + y, 720 / 10 * scl + x, 300 / 10 * scl + y, 720 / 10 * scl + x, 190 / 10 * scl + y, fill='white', outline='black', width='3'),
            canvas.create_line(675 / 10 * scl + x, 193 / 10 * scl + y, 675 / 10 * scl + x, 300 / 10 * scl + y, fill='black', width='3'),
            canvas.create_polygon(1000 / 10 * scl + x, 375 / 10 * scl + y, 1000 / 10 * scl + x, 455 / 10 * scl + y, 1054 / 10 * scl + x, 438 / 10 * scl + y, 1054 / 10 * scl + x, 368 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(1000 / 10 * scl + x, 375 / 10 * scl + y, 1000 / 10 * scl + x, 450 / 10 * scl + y, 1050 / 10 * scl + x, 435 / 10 * scl + y, 1050 / 10 * scl + x, 368 / 10 * scl + y, fill='white', outline='black', width='3'),
            #Веранда
            canvas.create_polygon(255 / 10 * scl + x, 489 / 10 * scl + y, 200 / 10 * scl + x, 520 / 10 * scl + y, 325 / 10 * scl + x, 545 / 10 * scl + y, 380 / 10 * scl + x, 510 / 10 * scl + y, fill='#c1bba4', outline='black'),
            canvas.create_polygon(200 / 10 * scl + x, 520 / 10 * scl + y, 200 / 10 * scl + x, 530 / 10 * scl + y, 325 / 10 * scl + x, 555 / 10 * scl + y, 325 / 10 * scl + x, 545 / 10 * scl + y, fill='#c1bba4', outline='black'),
            canvas.create_polygon(380 / 10 * scl + x, 510 / 10 * scl + y, 325 / 10 * scl + x, 545 / 10 * scl + y, 325 / 10 * scl + x, 555 / 10 * scl + y, 380 / 10 * scl + x, 520 / 10 * scl + y, fill='#c1bba4', outline='black'),
            canvas.create_polygon(315 / 10 * scl + x, 543 / 10 * scl + y, 325 / 10 * scl + x, 545 / 10 * scl + y, 325 / 10 * scl + x, 350 / 10 * scl + y, 315 / 10 * scl + x, 350 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(325 / 10 * scl + x, 350 / 10 * scl + y, 325 / 10 * scl + x, 545 / 10 * scl + y, 335 / 10 * scl + x, 538 / 10 * scl + y, 335 / 10 * scl + x, 350 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(200 / 10 * scl + x, 520 / 10 * scl + y, 210 / 10 * scl + x, 522 / 10 * scl + y, 210 / 10 * scl + x, 380 / 10 * scl + y, 200 / 10 * scl + x, 380 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(210 / 10 * scl + x, 380 / 10 * scl + y, 210 / 10 * scl + x, 522 / 10 * scl + y, 218 / 10 * scl + x, 516 / 10 * scl + y, 218 / 10 * scl + x, 380 / 10 * scl + y, fill='#d2691e', outline='black'),
            canvas.create_polygon(240 / 10 * scl + x, 333 / 10 * scl + y, 170 / 10 * scl + x, 374 / 10 * scl + y, 325 / 10 * scl + x, 387 / 10 * scl + y, 395 / 10 * scl + x, 343 / 10 * scl + y, fill='#c1bba4', outline='black'),
            canvas.create_polygon(170 / 10 * scl + x, 374 / 10 * scl + y, 170 / 10 * scl + x, 383 / 10 * scl + y, 325 / 10 * scl + x, 395 / 10 * scl + y, 325 / 10 * scl + x, 385 / 10 * scl + y, fill='#c1bba4', outline='black'),
            canvas.create_polygon(325 / 10 * scl + x, 385 / 10 * scl + y, 325 / 10 * scl + x, 395 / 10 * scl + y, 395 / 10 * scl + x, 353 / 10 * scl + y, 395 / 10 * scl + x, 343 / 10 * scl + y,fill='#c1bba4', outline='black'),

        canvas.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    root.geometry("1000x1000")
    app = Example(root)
    root.minsize(1240, 700)
    root.resizable(True, True)

    root.mainloop()

main()
