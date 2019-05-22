"""
插入排序
原理理解:就好像洗牌,把手里的牌分为两部分,一部分是有序的,另一部分是无序的,不断地从无序的牌中把牌拿出来,并插入到有序的序列中
1. 总共排序次数是n-1次，因为第一个默认是有序的，不需要排序
2. 每次都从无序的序列中拿一张牌，然后不断地和有序的牌做对比，并替换到合适的位置
3. 插入排序和冒泡排序有什么区别呢?插入排序如果key比前一个数要大,那么就直接break了,而冒泡排序还需要一个一个向前比对
"""
import random


def insert_sort(array):
    a_len = len(array)
    for x in range(1, a_len):
        key = array[x]
        j = x - 1
        while j > -1:
            if key < array[j]:
                array[j+1],array[j] =  array[j],key
                j -= 1
            else:
                break
    return array


if __name__ == '__main__':
    exp = random.sample(range(100), 100)
    rst = insert_sort(exp)
    print(rst)
