import random


def bubble_sort(array):
    a_len = len(array)
    for x in range(a_len -1):
        for j in range(1, a_len - x):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array


if __name__ == '__main__':
    exp = random.sample(range(100),100)
    rst = bubble_sort(exp)
    print(rst)
