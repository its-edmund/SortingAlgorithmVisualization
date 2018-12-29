import random
import time
from tkinter import *


class Sorter:
    bar_display = None
    height = 600
    width = 800
    randList = []
    master = None

    def __init__(self, master):
        self.master = master
        self.bar_display = Canvas(master, width=self.width, height=self.height, highlightthickness=0, bg="black")
        self.master.title("Sorting")
        self.master.geometry(str(self.width) + "x" + str(self.height))
        self.master.config(background='black')
        self.randList = self.generate_list(100)
        print(self.randList)
        self.draw(self.randList)
        self.bubble_sort(self.randList)

    def generate_list(self, num):
        list = []
        while len(list) != num:
            rand = random.randint(1, num)
            if not rand in list:
                list.append(rand)
        return list

    def draw(self, list):
        self.bar_display.delete("all")
        for num in list:
            self.bar_display.create_rectangle(list.index(num) * (self.width / len(list)),
                                              self.height - (num * self.height / len(list)),
                                              list.index(num) * (self.width / len(list)) + (
                                                      self.width / len(list)), self.height, fill='white')
            self.bar_display.pack()
        self.master.update()


    def bubble_sort(self, list):
        length_list = len(list)
        while (length_list != 0):
            new_length_list = 0
            self.draw(list)
            self.bar_display.after(50)
            for index in range(1, length_list):
                if list[index-1] > list[index]:
                    temp = list[index-1]
                    list[index-1] = list[index]
                    list[index] = temp
                    new_length_list = index
            length_list = new_length_list

def main():
    root = Tk()
    my_gui = Sorter(root)
    root.mainloop()


if __name__ == '__main__':
    main()
