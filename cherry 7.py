from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Cherry 7")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(0, 0, 1200, 1200, fill='white')

        # Cherry7
        # Фон
        canvas.create_rectangle(0, 0, 1200, 1200, fill='#96b62e')
        canvas.create_polygon(600, 0, 0, 600, 750, 550, 950, 0, fill='gray', outline='black', width='10')
        # Колесо 1
        canvas.create_polygon(335, 380, 350, 411, 380, 411, 380, 340, fill='black')
        canvas.create_oval(365, 360, 390, 410, fill='#393939', outline='black', width='2')
        canvas.create_arc(331, 360, 380, 410, start=180, extent=100, fill='black')
        # Капот
        canvas.create_polygon(400, 225, 320, 300, 653, 305, 710, 225, fill='#5e052a', outline='black')
        canvas.create_line(405, 298, 440, 245)
        canvas.create_line(562, 301, 605, 250)
        # Крыша
        canvas.create_polygon(475, 95, 428, 130, 695, 130, 740, 95, fill='#5e052a', outline='black')
        # Левое зеркало
        canvas.create_polygon(383, 204, 384, 223, 410, 225, 410, 205, fill='#1f1f1f', outline='black')
        canvas.create_line(386, 214, 402, 215, fill='black')
        # Колесо 3 - 1
        canvas.create_rectangle(735, 215, 763, 265, fill='black')
        # Колесо 2 - 1
        canvas.create_rectangle(661, 345, 695, 405, fill='black')
        canvas.create_arc(640, 345, 695, 405, start=180, extent=100, fill='black')
        # Перед
        canvas.create_polygon(320, 300, 318, 360, 650, 365, 653, 305, fill='#5e052a', outline='black')
        # Радиатор
        canvas.create_polygon(405, 298, 402, 352, 560, 355, 562, 301, fill='#b6c0c3', outline='black')
        canvas.create_polygon(412, 305, 409, 345, 553, 348, 555, 308, fill='black', outline='black')
        canvas.create_line(416, 338, 547, 342, fill='#b6c0c3', width='2')
        canvas.create_line(417, 329, 547, 333, fill='#b6c0c3', width='2')
        canvas.create_line(418, 320, 548, 324, fill='#b6c0c3', width='2')
        canvas.create_line(419, 312, 548, 315, fill='#b6c0c3', width='2')
        canvas.create_polygon(480, 318, 480, 332, 489, 332, 490, 318, fill='#b6c0c3', outline='black')
        # Фары
        canvas.create_polygon(330, 310, 328, 345, 403, 347, 405, 312, fill='#FFDEAD', outline='black', width='4')
        canvas.create_polygon(562, 312, 560, 350, 643, 352, 645, 314, fill='#FFDEAD', outline='black', width='4')
        # Габариты
        canvas.create_polygon(330, 310, 328, 345, 343, 345, 345, 310, fill='#D2691E', outline='black', width='3')
        canvas.create_polygon(630, 314, 628, 352, 643, 352, 645, 314, fill='#D2691E', outline='black', width='3')
        # Бок
        canvas.create_polygon(689, 230, 710, 226, 772, 138, 755, 133, fill='#5e052a')
        canvas.create_polygon(653, 305, 650, 390, 771, 210, 772, 138, fill='#5e052a', outline='black')
        canvas.create_line(653, 320, 772, 148)
        canvas.create_line(735, 176, 738, 185)
        canvas.create_line(738, 185, 738, 255)
        canvas.create_line(700, 215, 705, 230)
        canvas.create_line(705, 230, 705, 310)
        canvas.create_line(760, 140, 763, 152)
        canvas.create_line(763, 152, 763, 195)
        canvas.create_polygon(653, 375, 650, 390, 771, 210, 772, 195, fill='#1f1f1f')
        canvas.create_polygon(728, 208, 727, 218, 733, 208, 734, 198, fill='black', outline='#b6c0c3', width='2')
        canvas.create_polygon(755, 165, 756, 170, 760, 165, 761, 156, fill='black', outline='#b6c0c3', width='2')
        canvas.create_oval(734, 213, 738, 222, fill='#b6c0c3', outline='black')
        # Колесо 3 - 2
        canvas.create_oval(745, 199, 773, 260, fill='black')
        canvas.create_oval(742, 192, 773, 260, outline='black')
        canvas.create_oval(747, 205, 773, 265, fill='white')
        canvas.create_oval(751, 210, 768, 260, fill='black')
        # Колесо 2 - 2
        canvas.create_oval(670, 285, 709, 395, outline='black')
        canvas.create_oval(672, 295, 710, 405, fill='black')
        canvas.create_oval(677, 305, 710, 405, fill='white')
        canvas.create_oval(682, 312, 703, 398, fill='black')
        # Поворотник
        canvas.create_polygon(657, 323, 657, 333, 665, 320, 665, 310, fill='#D2691E', outline='black')
        # Лобовое стекло
        canvas.create_polygon(430, 130, 400, 225, 690, 225, 686, 130, fill='#d3d3d3', outline='black', width='3')
        # Боковое стекло
        canvas.create_polygon(695, 130, 700, 215, 735, 172, 720, 110, fill='#d3d3d3', outline='black', width='2')
        canvas.create_polygon(720, 110, 735, 172, 760, 140, 740, 95, fill='#d3d3d3', outline='black', width='2')
        canvas.create_line(733, 176, 717, 112, fill='#5e052a', width='5')
        # Правое зеркало
        canvas.create_polygon(705, 200, 695, 225, 720, 215, 727, 195, fill='#1f1f1f')
        canvas.create_polygon(686, 100, 691, 225, 700, 225, 693, 100, fill='#5e052a')
        canvas.create_line(700, 212, 722, 205)
        # Бампер
        canvas.create_polygon(319, 360, 310, 370, 655, 376, 660, 365, fill='#1f1f1f', outline='black')
        canvas.create_polygon(310, 370, 312, 390, 655, 395, 655, 376, fill='#1f1f1f', outline='black')
        canvas.create_polygon(334, 360, 325, 370, 640, 376, 645, 365, fill='#b6c0c3', outline='black')
        canvas.create_polygon(655, 376, 655, 395, 660, 388, 660, 365, fill='#1f1f1f', outline='black')
        canvas.create_polygon(772, 180, 771, 200, 774, 197, 775, 179, fill='#1f1f1f', outline='black')

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
