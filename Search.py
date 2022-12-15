from InsertionSort import *


def contains(my_list, element):
    for e in my_list:
        if e == element:
            return True
        elif e > element:
            return False
    return False


def main():
    my_list = [9, 35, 10, 18, 3, 7, 12, 14, 36, 34]
    insertion_sort(my_list)
    print(my_list)
    print(contains(my_list, 4))


if __name__ == "__main__":
    main()
