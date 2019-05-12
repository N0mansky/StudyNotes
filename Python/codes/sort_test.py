def insert_sort(lists):
    counts = len(lists)
    for i in range(1, counts):
        key = lists[i]
        j = i - 1
        while j > -1:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


def shell_sort(lists):
    increment = count = len(lists)
    while increment > 1:
        increment = increment // 3 + 1
        for x in range(increment, count):
            key = lists[x]
            j = x - increment
            while j >= 0:
                if lists[j] > key:
                    lists[j + increment] = lists[j]
                    lists[j] = key
                j -= increment
    return lists


if __name__ == '__main__':
    a = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    b = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
    # c=insert_sort(a)
    shell_sort(a)
    print("List a is {}".format(a))
    print("List b is {}".format(b))
    assert a == b, 'Not equal!!!'
