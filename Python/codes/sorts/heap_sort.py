"""
# 堆排序
## 原理:
1. 三个节点组成一个堆
2. 父节点比子节点都大的叫最大堆
3. 父节点比子节点都小的叫最小堆
3. 由于组成的堆和完全二叉树差不多,所以如果父节点的index是i,那么左子节点的index为2i,右子节点的index为2i+1

## 单调不减算法步骤:
### 步骤1:
     - 创建一个最大堆,不断地比较子节点和父节点
     - 如果子节点比父节点大,那么交换子节点和父节点
     - 这样的话,就确保了根节点是整个序列中最大的节点

### 步骤2:
     - 不断地将根节点放到这棵树的最后面,从而整个数组都是有序的了
"""
import random

"""
非递归的方法
"""


def heap_sort(array):
    if not array:
        return []
    sz = len(array)

    def build_heap(array, size):
        # 循环创建堆,确保每个节点都比其左子节点和右子节点都要大
        # 为什么只循环到size的一半呢?因为叶子节点的总数等于非叶子节点的总数,或者比非叶子节点的总数+1
        # 所以如果index大于size的一半,那么这个节点肯定就是叶子节点了
        for x in range(size // 2 - 1, -1, -1):
            # 比较哪个数是最大的
            left = x * 2 + 1
            right = x * 2 + 2
            if left < size and array[left] > array[x]:
                array[x], array[left] = array[left], array[x]
            if right < size and array[right] > array[x]:
                array[x], array[right] = array[right], array[x]
        return array

    build_heap(array, sz)
    while sz > 0:
        array[0], array[sz - 1] = array[sz - 1], array[0]
        sz -= 1
        build_heap(array, sz)


"""
递归的方法
原理差不多，不过这个是通过递归不断的把小的节点下沉
"""


def heap_sort2(array):
    def build_heap(array, size):
        for x in range(size // 2 - 1, -1, -1):
            adjust_heap(array, x, size)

    def adjust_heap(array, x, size):
        left = x * 2 + 1
        right = x * 2 + 2
        max_idx = x
        if max_idx < size // 2:
            if left < size and array[left] > array[max_idx]:
                max_idx = left
            if right < size and array[right] > array[max_idx]:
                max_idx = right
            if max_idx != x:
                array[max_idx], array[x] = array[x], array[max_idx]
                adjust_heap(array, max_idx, size)

    size = len(array)
    build_heap(array, size)
    for x in range(size - 1, 0, -1):
        array[0], array[x] = array[x], array[0]
        adjust_heap(array, 0, x)


if __name__ == '__main__':
    exp = random.sample(range(100), 100)
    expect = [x for x in range(100)]
    heap_sort2(exp)
    print(exp)
    assert exp == expect
