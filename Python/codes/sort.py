def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j > -1:
            if lists[j] > key:
                lists[j + 1], lists[j] = lists[j], key
            j -= 1
    return lists


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


def bubble_sort(lists):
   count = len(lists)
   for i in range(count - 1):
       for j in range(1, count - i):
           if lists[j - 1] > lists[j]:
               lists[j - 1], lists[j] = lists[j], lists[j - 1]
   return lists

#def bubble_sort(lists):
#    count = len(lists)
#    for i in range(count - 1):
#        for j in range(i + 1, count):
#            if lists[i] > lists[j]:
#                lists[i], lists[j] = lists[j], lists[i]
#    return lists

# Big heap of root
def heap_sort(lists):

    def build_head(lists,size):
        for i in reversed(range(0,(size//2))):
            adjust_heap(lists,i,size)

    def adjust_heap(lists,i,size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max = i
        if i < size //2:
            if lchild < size and lists[lchild] > lists[max]:
                max = lchild
            if rchild < size and lists[rchild] > lists[max]:
                max = rchild
            if max != i:
                lists[max],lists[i] = lists[i],lists[max]
                adjust_heap(lists,max,size)

    size = len(lists) # Get the size of lists
    build_head(lists,size) # Step one,build heap
    for i in reversed(range(size)):
        lists[0] ,lists[i] = lists[i],lists[0]
        adjust_heap(lists,0,i)

# Smail heap of root
def heap_sort2(lists):
    def build_heap(lists,size):
        # Because leaf node doesn't have child,then don't need  heapify
        # The last non-leaf node is size//2
        for x in reversed(range(size//2)):
            heapify(lists,x,size)

    def heapify(lists,x,size):
        ltree = 2*x + 1
        rtree = 2*x + 2
        min = x
        if x < size //2:
            if ltree < size and  lists[ltree] < lists[min]:
                min = ltree
            if rtree < size and lists[rtree] < lists[min]:
                min = rtree
            if min != x:
                lists[x],lists[min] = lists[min],lists[x]
                heapify(lists,min,size)


    size = len(lists) # Get current lists's size
    build_heap(lists,size) # Initiate heap and make sure all parents smailer than child
    for x in reversed(range(size)):
        lists[0],lists[x] = lists[x],lists[0]
        heapify(lists,0,x)



if __name__ == '__main__':
    a = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    b = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
    # c=shell_sort(a)
    # insert_sort(a)
    # shell_sort(a)
    # bubble_sort(a)
    # heap_sort(a)
    heap_sort2(a)
    print("Arrya a is {}".format(a))
    print("Arrya b is {}".format(b))
    assert a == b, 'Error'
