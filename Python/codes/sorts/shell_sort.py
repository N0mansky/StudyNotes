"""
希尔排序
思路:
1. 插入排序相当于一副牌,分为两部分,一部分是有序序列,另一部分是无序的序列,然后不断地从无序序列中拿出牌放到有序序列中
2. 而希尔排序是直接插入排序的改进版本,他是把一副牌分为多个部分,然后对每个部分进行选择排序,从而减小交换跨度
"""
import random


def shell_sort(array):
    gap=a_len = len(array)
    while gap > 1:
        gap = gap // 3 + 1
        for x in range(gap, a_len, gap):
            key = array[x]
            j = x - gap
            while j > -1:
                if array[j] > key:
                    array[j], array[j + gap] = key, array[j]
                    j -= gap
                else:
                    break
    return array


if __name__ == '__main__':
    exp = random.sample(range(100), 100)
    shell_sort(exp)
    print(exp)
