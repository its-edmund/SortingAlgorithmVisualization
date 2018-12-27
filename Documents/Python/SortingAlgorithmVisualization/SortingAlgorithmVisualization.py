import random
from tkinter import *

class Sorter:

    height = 800
    width = 1000
    randList = []

    def __init__(self, master):
        self.master = master
        master.title("Sorting")
        master.geometry(self.width + "x" + self.height)
        master.config(background = 'black')
        randList = generate_list(100)
        draw(master)

    def generate_list(num):
        list = []
        while len(list) != num:
            rand = random.randint(1,num)
            if not rand in list:
                list.append(rand)
        return list

    def draw(list, window):
        top = tkinter.Tk()
        top.mainloop()
        for num in list:
            canvas = Canvas(master, width=width/len(randList), height=(height/len(randList))*num)
            canvas.pack()


root = Tk()
my_gui = Sorter(root)
root.mainloop()
