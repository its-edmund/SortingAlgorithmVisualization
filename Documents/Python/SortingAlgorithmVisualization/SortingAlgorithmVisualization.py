import random
from tkinter import *

class Sorter:

    height = 800
    width = 1000
    randList = []

    def __init__(self, master):
        self.master = master
        master.title("Sorting")
        master.geometry(str(self.width) + "x" + str(self.height))
        master.config(background = 'black')
        self.randList = self.generate_list(100)
        self.draw(self.randList, master)

    def generate_list(self, num):
        list = []
        while len(list) != num:
            rand = random.randint(1,num)
            if not rand in list:
                list.append(rand)
        return list

    def draw(self, list, window):
        for num in list:
            canvas = Canvas(window, width=self.width/len(self.randList), height=(self.height/len(self.randList))*num)
            canvas.pack()


root = Tk()
my_gui = Sorter(root)
root.mainloop()
