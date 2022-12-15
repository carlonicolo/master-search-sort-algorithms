def sort(unsorted_list):
    # takes an unsorted list as input and returns a new list with the elements sorted
    sorted_list = []

    while len(unsorted_list) > 0:
        smallest = unsorted_list[0]
        for element in unsorted_list:
            if element < smallest:
                smallest = element
        sorted_list.append(smallest)
        unsorted_list.remove(smallest)

    return sorted_list


def main():
    unsorted_list = [3, 5, 1, 9, 7, 2, 10, 4, 8, 6]
    sorted_list = sort(unsorted_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
