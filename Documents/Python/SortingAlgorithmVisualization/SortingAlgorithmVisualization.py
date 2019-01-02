import random
import time
from tkinter import *
from abc import ABC, abstractmethod


class Sorter:
    bar_display = None
    height = 600
    width = 800
    randList = []
    oldRandList = []
    master = None
    algorithm_processing = None

    def __init__(self, master):
        self.master = master
        self.bar_display = Canvas(master, width=self.width, height=self.height, highlightthickness=0, bg="black")
        self.master.title("Sorting")
        self.master.geometry(str(self.width) + "x" + str(self.height))
        self.master.config(background='black')
        self.randList = self.generate_list(50)
        self.oldRandList = [range(1,len(self.randList))]

    def set_algorithm(self, algorithm):
        self.algorithm_processing = algorithm

    def generate_list(self, num):
        list = []
        while len(list) != num:
            rand = random.randint(1, num)
            if not rand in list:
                list.append(rand)
        return list

    """def draw(self, list):
        self.bar_display.delete("all")
        self.bar_display.pack()
        for num in list:
            self.bar_display.create_rectangle(list.index(num) * (self.width / len(list)),
                                              self.height - (num * self.height / len(list)),
                                              list.index(num) * (self.width / len(list)) + (
                                                      self.width / len(list)), self.height, fill='white')
        self.master.update()"""

    def draw(self, list, oldList=None):
        if oldList is None:
            self.bar_display.delete("all")
            self.bar_display.pack()
            for num in list:
                #if num not in oldList or list.index(num) != oldList.index(num):
                self.bar_display.create_rectangle(list.index(num) * (self.width / len(list)),
                                                  self.height - (num * self.height / len(list)),
                                                  list.index(num) * (self.width / len(list)) + (
                                                          self.width / len(list)), self.height, fill='white')
        else:
            self.bar_display.delete("all")
            self.bar_display.pack()
            for num in list:
                if num not in oldList or list.index(num) != oldList.index(num):
                    self.bar_display.create_rectangle(list.index(num) * (self.width / len(list)),
                                                      self.height - (num * self.height / len(list)),
                                                      list.index(num) * (self.width / len(list)) + (
                                                              self.width / len(list)), self.height, fill='white')
        self.master.update()

    def draw_with_red(self, list, index, oldList=None):
        tempList = list
        if oldList is None:
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
        else:
            self.bar_display.delete("all")
            for num in tempList:
                if num not in oldList or tempList.index(num) != oldList.index(num):
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

    def draw_algorithm(self):
        for i in range(0,self.algorithm_processing.length_list):
            self.draw(self.algorithm_processing.step())
            self.bar_display.after(25)

    def pulse(self,list):
        self.draw(list)
        for i in range(0, len(list)+1):
            self.draw_with_red(list, range(0,i))


class SortingAlgorithm(ABC):

    list = []
    length_list = 0

    def __init__(self, list):
        self.list = list
        self.length_list = len(list)

    @abstractmethod
    def step(self):
        return

    @abstractmethod
    def sort(self):
        return


class BubbleSort(SortingAlgorithm):

    new_length_list = 0

    def __init__(self, list):
        super().__init__(list)

    def set_list(self, list):
        self.list = list

    def get_list(self):
        return self.list

    def step(self):
        self.new_length_list = 0
        index = 1
        for index in range(1, self.length_list):
            if self.list[index - 1] > self.list[index]:
                temp = self.list[index - 1]
                self.list[index - 1] = self.list[index]
                self.list[index] = temp
                self.new_length_list = index
        self.length_list = self.new_length_list
        return self.list

    def sort(self):
        while True:
            self.step()
            if self.length_list is 0:
                return self.list


class CocktailShakerSort(SortingAlgorithm):

    beg_Index = 0
    end_Index = 0
    new_Beg_Index = 0
    new_End_Index = 0

    def __init__(self, list):
        super().__init__(list)
        self.beg_Index = 0
        self.end_Index = len(self.list)-2

    def step(self):
        self.new_Beg_Index = self.end_Index
        self.new_End_Index = self.beg_Index
        for i in range(self.beg_Index, self.end_Index):
            if self.list[i] > self.list[i + 1]:
                temp = self.list[i + 1]
                self.list[i + 1] = self.list[i]
                self.list[i] = temp
                self.new_End_Index = i
                self.drawingList = list
        self.end_Index = self.new_End_Index + 1;
        for i in range(self.end_Index, self.beg_Index, -1):
            if self.list[i] > self.list[i + 1]:
                temp = self.list[i + 1]
                self.list[i + 1] = self.list[i]
                self.list[i] = temp
                self.new_Beg_Index = i
        self.beg_Index = self.new_Beg_Index - 1
        return self.list

    def sort(self):
        while self.beg_Index <= self.end_Index:
            self.step()
        return self.list


def main():
    root = Tk()
    sorter = Sorter(root)
    cs = CocktailShakerSort(sorter.generate_list(200))
    bs = BubbleSort(sorter.generate_list(200))
    sorter.set_algorithm(cs)
    sorter.draw_algorithm()
    root.mainloop()


if __name__ == '__main__':
    main()
