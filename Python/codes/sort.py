import math


def shell_sort(lists):
    gap = count = len(lists)
    while gap > 1:
        gap = gap // 3 + 1
        for i in range(0, count, gap):
            for j in range(i + gap, count, gap):
                if lists[j] < lists[i]:
                    lists[i], lists[j] = lists[j], lists[i]
    return lists


def select_sort(lists):
    count = len(lists)
    for i in range(count - 1):
        min = i
        for j in range(i, count):
            if lists[j] < lists[min]:
                min = j
        lists[i], lists[min] = lists[min], lists[i]
    return lists




# Big heap of root
def heap_sort(lists):
    def build_head(lists, size):
        for i in reversed(range(0, (size // 2))):
            adjust_heap(lists, i, size)

    def adjust_heap(lists, i, size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max = i
        if i < size // 2:
            if lchild < size and lists[lchild] > lists[max]:
                max = lchild
            if rchild < size and lists[rchild] > lists[max]:
                max = rchild
            if max != i:
                lists[max], lists[i] = lists[i], lists[max]
                adjust_heap(lists, max, size)

    size = len(lists)  # Get the size of lists
    build_head(lists, size)  # Step one,build heap
    for i in reversed(range(size)):
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)


# Smail heap of root
def heap_sort2(lists):
    def build_heap(lists, size):
        # Because leaf node doesn't have child,then don't need  heapify
        # The last non-leaf node is size//2
        for x in reversed(range(size // 2)):
            heapify(lists, x, size)

    def heapify(lists, x, size):
        ltree = 2 * x + 1
        rtree = 2 * x + 2
        min = x
        if x < size // 2:
            if ltree < size and lists[ltree] < lists[min]:
                min = ltree
            if rtree < size and lists[rtree] < lists[min]:
                min = rtree
            if min != x:
                lists[x], lists[min] = lists[min], lists[x]
                heapify(lists, min, size)

    size = len(lists)  # Get current lists's size
    build_heap(lists, size)  # Initiate heap and make sure all parents smailer than child
    for x in reversed(range(size)):
        lists[0], lists[x] = lists[x], lists[0]
        heapify(lists, 0, x)


# Merge sort
def merge_sort(lists):
    def merge(arr, left, mid, right):
        left_size = mid - left
        right_size = right - mid + 1

        l1 = []
        r1 = []

        for x in range(left, mid):
            l1.append(arr[x])
        for x in range(mid, right + 1):
            r1.append(arr[x])
        i = j = 0
        k = left
        while i < left_size and j < right_size:
            if l1[i] < r1[j]:
                arr[k] = l1[i]
                i += 1
                k += 1
            else:
                arr[k] = r1[j]
                j += 1
                k += 1
        while i < left_size:
            arr[k] = l1[i]
            k += 1
            i += 1
        while j < right_size:
            arr[k] = r1[j]
            k += 1
            j += 1

    def recur(arr, left, right):
        if left == right:
            return
        mid = (left + right) // 2
        recur(arr, left, mid)
        recur(arr, mid + 1, right)
        merge(arr, left, mid + 1, right)

    size = len(lists)
    recur(lists, 0, size - 1)


def merge_sort2(lists):
    def merge(llist, rlist):
        rst = []
        # i = j = 0
        # while i < len(llist) and j < len(rlist):
        while llist and rlist:
            if llist[0] < rlist[0]:
                rst.append(llist.pop(0))
            else:
                rst.append(rlist.pop(0))
        rst.extend(llist)
        rst.extend(rlist)
        return rst

    def recur(lists):
        if len(lists) <= 1:
            return lists
        mid = len(lists) // 2
        left = recur(lists[:mid])
        right = recur(lists[mid:])
        return merge(left, right)

    return recur(lists)


def radix_sort(lists):
    # Create a bucket to store value
    bucket = [[] for x in range(10)]
    for x in range(1, 10):
        mod = 10 ** x
        divisor = 10 ** (x - 1)
        for x in lists:
            val = x % mod // divisor
            bucket[val].append(x)
        lists = []
        rst = 0
        for x in bucket:
            if x:
                rst += 1
            while x:
                lists.append(x.pop(0))
        if x == 1:
            break
    return lists


def radix_sort2(lists, radix=10):
    k = math.ceil(math.log(max(lists), radix))
    bucket = [[] for x in range(radix)]
    for x in range(1, k + 1):
        for j in lists:
            bucket[j % (10 ** x) // (10 ** (x - 1))].append(j)
        del lists[:]
        for z in bucket:
            lists += z[:]
            del z[:]
    return lists


if __name__ == '__main__':
    a = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    b = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
    # c=shell_sort(a)
    # insert_sort(a)
    # shell_sort(a)
    # bubble_sort(a)
    # heap_sort(a)
    # heap_sort2(a)
    # a = merge_sort2(a)
    a = radix_sort2(a)
    print("Arrya a is {}".format(a))
    print("Arrya b is {}".format(b))
    assert a == b, 'Error'
