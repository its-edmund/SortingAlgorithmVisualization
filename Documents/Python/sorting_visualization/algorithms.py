from abc import ABC, abstractmethod

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

    def generate_list(self, num=100):
        self.list = []
        while len(list) != num:
            rand = random.randint(1, num)
            if not rand in list:
                list.append(rand)
        return list


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