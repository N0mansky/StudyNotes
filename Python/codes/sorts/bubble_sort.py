"""
原理理解:类似于泡泡浮出水面,不断的把最大的数放到数组的最后面
1. 泡泡总共需要浮出n-1次,n是数的个数,为什么是n-1呢,因为把1个到n-1个数依次放到了最后,那么自然第0个也就是最小的了
2. 每个泡泡总共需要比较n-m-2(n是总的数个数,m是已经排列好的数的个数,-2是因为需要数组最大下表为n-1,然后每次比较需要两个数,所以还需要减1)次,
   因为已经跑过得次数大的泡泡肯定都放到最后面了,也就没有必要比了
3. Time-complexity 为O(n^2)
"""

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
