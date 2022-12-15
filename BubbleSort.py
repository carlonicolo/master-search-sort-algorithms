def bubble_sort(my_list):
    for i in range(len(my_list), 1, -1):
        for j in range(1, i):
            if my_list[j-1] > my_list[j]:
                my_list[j-1], my_list[j] = my_list[j], my_list[j-1]


def main():
    my_list = [3, 5, 1, 9, 7, 2, 10, 4, 8, 6]
    print(my_list)
    bubble_sort(my_list)
    print(my_list)


if __name__ == "__main__":
    main()
