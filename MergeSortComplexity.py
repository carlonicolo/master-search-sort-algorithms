import random


def generate_random_list(n):
    # n is the length of the list
    my_list = []
    for i in range(n):
        my_list.append(random.randint(0, 4*n))
    return my_list


def insertion_sort(my_list):
    cnt = 0
    for i in range(1, len(my_list)):
        for j in range(i, 0, -1):
            cnt += 1
            if my_list[j] < my_list[j-1]:
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            else:
                break
    return cnt


def merge_sort(my_list):
    if len(my_list) <= 1:
        return 1

    mid = len(my_list)//2
    left_list = my_list[:mid]
    right_list = my_list[mid:]

    cnt = merge_sort(left_list)
    cnt += merge_sort(right_list)

    # insert the merge sorting here
    index_left = 0
    index_right = 0
    index_main = 0

    while index_left < len(left_list) and index_right < len(right_list):
        cnt += 1
        if right_list[index_right] < left_list[index_left]:
            my_list[index_main] = right_list[index_right]
            index_right += 1
            index_main += 1
        else:
            my_list[index_main] = left_list[index_left]
            index_left += 1
            index_main += 1

    while index_left < len(left_list):
        cnt += 1
        my_list[index_main] = left_list[index_left]
        index_left += 1
        index_main += 1

    while index_right < len(right_list):
        cnt += 1
        my_list[index_main] = right_list[index_right]
        index_right += 1
        index_main += 1

    return cnt


def main():
    it = 100
    print("length:    merge sort:   insertion sort:")
    for n in range(5, 101, 5):
        cnt_merge_sort = 0
        cnt_insert_sort = 0
        for i in range(it):

            my_list = generate_random_list(n)
            cnt_merge_sort += merge_sort(my_list)

            my_list = generate_random_list(n)
            cnt_insert_sort += insertion_sort(my_list)

        print('{:<4d}{:>13.2f}{:>13.2f}'.format(n, cnt_merge_sort/it, cnt_insert_sort/it))


if __name__ == "__main__":
    main()