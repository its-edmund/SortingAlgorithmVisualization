import random
import time
from tkinter import *


class Sorter:
    bar_display = None
    height = 600
    width = 800
    randList = []
    oldRandList = []
    master = None

    def __init__(self, master):
        self.master = master
        self.bar_display = Canvas(master, width=self.width, height=self.height, highlightthickness=0, bg="black")
        self.master.title("Sorting")
        self.master.geometry(str(self.width) + "x" + str(self.height))
        self.master.config(background='black')
        self.randList = self.generate_list(50)
        self.oldRandList = [range(1,len(self.randList))]

        self.draw(self.randList, self.oldRandList)
        #self.cocktail_shaker_sort(self.randList, self.oldRandList)
        self.bubble_sort(self.randList, self.oldRandList)
        self.pulse(self.randList)
        self.randList = self.generate_list(50)
        self.oldRandList = [range(1, len(self.randList))]
        self.draw(self.randList, self.oldRandList)
        self.cocktail_shaker_sort(self.randList, self.oldRandList)
        self.pulse(self.randList)

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

    def pulse(self,list):
        self.draw(list)
        for i in range(0, len(list)+1):
            self.draw_with_red(list, range(0,i))

    def bubble_sort(self, list, oldList):
        self.oldRandList = self.randList
        length_list = len(list)
        while (length_list != 0):
            new_length_list = 0
            index = 1
            for index in range(1, length_list):

                if list[index - 1] > list[index]:
                    temp = list[index - 1]
                    list[index - 1] = list[index]
                    list[index] = temp
                    new_length_list = index
                self.draw_with_red(list, [index, index-1], oldList)
            length_list = new_length_list

    def cocktail_shaker_sort(self, list, oldList):
        begIndex = 0
        endIndex = len(list)-2
        while begIndex <= endIndex:
            newBegIndex = endIndex
            newEndIndex = begIndex
            for i in range(begIndex, endIndex):
                if list[i] > list[i + 1]:
                    temp = list[i + 1]
                    list[i + 1] = list[i]
                    list[i] = temp
                    newEndIndex = i
                self.draw_with_red(list, [i+1])
            endIndex = newEndIndex + 1;
            for i in range(endIndex,begIndex, -1):
                if list[i] > list[i + 1]:
                    temp = list[i + 1]
                    list[i + 1] = list[i]
                    list[i] = temp
                    newBegIndex = i
                self.draw_with_red(list, [i])
            begIndex = newBegIndex - 1

def main():
    root = Tk()
    my_gui = Sorter(root)
    root.mainloop()


if __name__ == '__main__':
    main()
