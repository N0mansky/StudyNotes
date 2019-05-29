"""
# 基数排序
## 思路
1. 基数排序是一种分配式排序,和桶排序比较类似
2. complexity
    - time:O(nlog(r)m)
3. 分别提取待排序的数字的部分值,然后分别放在对应的桶中,当所有的数字都在第一个桶中,则数组排序完成
"""
import random
import math

def radix_sort(array,radix=10):
    k = math.ceil(math.log(max(array),radix))
    bucket = [[] for x in range(radix)]
    for x in range(1,k+1):
        for j in array:
            bucket[j %(10 ** x)//(10 ** (x-1))].append(j)
        del array[:]
        for z in bucket:
            array += z[:]
            del z[:]
    return array


if __name__ == '__main__':
    exp = random.sample(range(20), 20)
    expected = [x for x in range(20)]
    rst = radix_sort(exp)
    print(exp)
    print(rst)
    assert rst == expected
