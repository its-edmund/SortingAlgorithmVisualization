from .sorting_gui import *

def main():
    root = Tk()
    sorter = Sorter(root)
    cs = CocktailShakerSort(sorter.generate_list(200))
    bs = BubbleSort(sorter.generate_list(200))
    sorter.set_algorithm(bs)
    sorter.draw_algorithm()
    sorter.pulse()
    root.mainloop()


if __name__ == '__main__':
    main()