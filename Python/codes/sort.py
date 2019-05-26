import math

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
