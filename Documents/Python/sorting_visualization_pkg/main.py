from sorting_gui import *
from tkinter import *
import time


def main():
    root = Tk()
    sorter = Sorter(root)
    cs = CocktailShakerSort(50)
    bs = BubbleSort(50)
    ss = SelectionSort(50)
    sorter.set_algorithm(cs)
    sorter.set_algorithms([cs,bs,ss])
    cs.attach(sorter)
    bs.attach(sorter)
    ss.attach(sorter)
    start = time.time()
    sorter.running_algorithms()
    end = time.time()
    sorter.pulse()
    print(str(end-start) + " seconds")
    root.mainloop()


if __name__ == '__main__':
    main()