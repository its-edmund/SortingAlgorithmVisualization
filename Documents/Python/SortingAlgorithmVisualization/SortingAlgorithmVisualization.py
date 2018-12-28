import random
from tkinter import *


class Sorter:
    height = 600
    width = 800
    randList = []

    def __init__(self, master):
        self.master = master
        master.title("Sorting")
        master.geometry(str(self.width) + "x" + str(self.height))
        master.config(background='black')
        self.randList = self.generate_list(100)
        self.draw(self.randList, master)

    def generate_list(self, num):
        list = []
        while len(list) != num:
            rand = random.randint(1, num)
            if not rand in list:
                list.append(rand)
        return list

    def draw(self, list, window):
        canvas = Canvas(window, width=self.width, height=self.height, highlightthickness=0, bg="black")
        for num in list:
            canvas.create_rectangle(list.index(num) * (self.width / len(list)),
                                    self.height - (num * self.height / len(list)),
                                    list.index(num) * (self.width / len(list)) + (
                                            self.width / len(list)), self.height, fill='white')

            """list.index(num) * (self.width / len(list)), 150, list.index(num) * (self.width / len(list)) + (
                        len(list) / self.width), 0, fill = 'red'"""

            canvas.pack()

    def process_algorithm(self, algorithm_name, list):
        pass

def main():
    root = Tk()
    my_gui = Sorter(root)
    print(my_gui.randList)
    root.mainloop()


if __name__ == '__main__':
    main()
