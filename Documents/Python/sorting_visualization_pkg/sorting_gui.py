from tkinter import *
from algorithms import *
from observer_pattern import *


class Sorter(Observer):

    bar_display_rectangles = []
    bar_display = None
    height = 600
    width = 800
    oldRandList = []
    master = None
    algorithm = None
    algorithms = []

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.bar_display = Canvas(master, width=self.width, height=self.height, highlightthickness=0, bg="black")
        self.master.title("Sorting")
        self.master.geometry(str(self.width) + "x" + str(self.height))
        self.master.config(background='black')
        #self.randList = self.generate_list(50)
        #self.oldRandList = [range(1,len(self.randList))]

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def set_algorithms(self, algorithms):
        self.algorithms = algorithms




    """def draw(self, list):
        self.bar_display.delete("all")
        self.bar_display.pack()
        for num in list:
            self.bar_display.create_rectangle(list.index(num) * (self.width / len(list)),
                                              self.height - (num * self.height / len(list)),
                                              list.index(num) * (self.width / len(list)) + (
                                                      self.width / len(list)), self.height, fill='white')
        self.master.update()"""

    def draw(self, list):
        self.bar_display.delete("all")
        self.bar_display.pack()
        for num in list:
            rect = self.bar_display.create_rectangle(list.index(num) * (self.width / len(list)),
                                              self.height - (num * self.height / len(list)),
                                              list.index(num) * (self.width / len(list)) + (
                                                      self.width / len(list)), self.height, fill='white')
            self.bar_display_rectangles.append(rect)
        self.master.update()

    def draw_with_red(self, list, index):
        tempList = list
        self.bar_display.delete("all")
        for num in tempList:
            self.bar_display.create_rectangle(tempList.index(num) * (self.width / len(tempList)),
                                              self.height - (num * self.height / len(tempList)),
                                              tempList.index(num) * (self.width / len(tempList)) + (
                                                      self.width / len(tempList)), self.height, fill='white')
        for i in index:
            self.bar_display.create_rectangle(i * (self.width / len(tempList)),
                                              self.height - (tempList[i] * self.height / len(tempList)),
                                              i * (self.width / len(tempList)) + (
                                                      self.width / len(tempList)), self.height, fill='red')
        self.bar_display.pack()
        self.master.update()
        list = tempList

    """def update_display(self, index1, index2):
        temp = self.bar_display_rectangles[index1]
        self.bar_display_rectangles[index1] = self.bar_display_rectangles[index2]
        self.bar_display_rectangles[index2] = temp
        self.bar_display"""

    def draw_algorithm(self):
        for i in range(0, self.algorithm.length_list):
            self.algorithm.sort()

    def pulse(self):
        self.draw(self.algorithm.list)
        for i in range(0, len(self.algorithm.list) + 1):
            self.draw_with_red(self.algorithm.list, range(0, i))

    def update(self, list):
        self.draw(list)

    def running_algorithms(self):
        for algorithm in self.algorithms:
            self.set_algorithm(algorithm)
            self.draw(algorithm.list)
            self.draw_algorithm()
            self.pulse()
            self.bar_display.after(1000)
