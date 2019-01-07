from abc import ABC, abstractmethod
from observer_pattern import Subject
import random


class SortingAlgorithm(ABC, Subject):

    list = []
    length_list = 0

    def __init__(self, listlen=50):
        super().__init__()
        self.list = self.generate_list(listlen)
        self.length_list = listlen

    @abstractmethod
    def sort(self):
        pass

    def generate_list(self, num=100):
        list = []
        while len(list) != num:
            rand = random.randint(1, num)
            if rand not in list:
                list.append(rand)
        return list

    def _notify(self):
        for observer in self._observers:
            observer.update(self.list)


class BubbleSort(SortingAlgorithm):

    new_length_list = 0

    def __init__(self, listlen):
        super().__init__(listlen)
        #super().__init__(self.generate_list(listlen))

    def set_list(self, list):
        self.list = list

    def get_list(self):
        return self.list

    def sort(self):
        while True:
            self.new_length_list = 0
            index = 1
            for index in range(1, self.length_list):
                if self.list[index - 1] > self.list[index]:
                    self.list[index], self.list[index - 1] = self.list[index - 1], self.list[index]
                    self.new_length_list = index
                self._notify()
            self.length_list = self.new_length_list
            if self.length_list is 0:
                return


class CocktailShakerSort(SortingAlgorithm):

    beg_Index = 0
    end_Index = 0
    new_Beg_Index = 0
    new_End_Index = 0

    def __init__(self, list):
        super().__init__(list)
        self.beg_Index = 0
        self.end_Index = len(self.list)-2

    def set_list(self, list):
        self.list = list

    def get_list(self):
        return self.list

    def sort(self):
        while self.beg_Index <= self.end_Index:
            self.new_Beg_Index = self.end_Index
            self.new_End_Index = self.beg_Index
            for i in range(self.beg_Index, self.end_Index):
                if self.list[i] > self.list[i + 1]:
                    self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]
                    self.new_End_Index = i
                    self.drawingList = list
                self._notify()
            self.end_Index = self.new_End_Index + 1;
            for i in range(self.end_Index, self.beg_Index, -1):
                if self.list[i] > self.list[i + 1]:
                    self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
                    self.new_Beg_Index = i
                self._notify()
            self.beg_Index = self.new_Beg_Index - 1
            return
        return


class SelectionSort(SortingAlgorithm):

    min = 0

    def __init__(self, list):
        super().__init__(list)

    def set_list(self, list):
        self.list = list

    def get_list(self):
        return self.list

    def sort(self):
        for i in range(len(self.list)):
            self.min = i
            for j in range(i+1, len(self.list)):
                if self.list[j] < self.list[self.min]:
                    self.min = j
            self.list[i], self.list[self.min] = self.list[self.min], self.list[i]
            self._notify()
        return
