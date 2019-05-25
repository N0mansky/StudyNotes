"""
# 直接选择排序
---
## 定义:
> 第1趟，在待排序记录r[1] ~ r[n]中选出最小的记录，将它与r[1]交换；
> 第2趟，在待排序记录r[2] ~ r[n]中选出最小的记录，将它与r[2]交换；
> 以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，
> 使有序序列不断增长直到全部排序完毕
说人话就是: 就是不断从一个队伍中,每次都选出最矮的那个人,然后放在排好序的人的后面;
## 复杂度:
### 时间复杂度:
    - best: O(n²)
    - avg:  O(n²)
    - worst:O(n²)
### 空间复杂度:O(1)
"""

import random

def select_sort(array):
    sz = len(array)
    for x in range(sz-1):
        base = array[x]
        for y in range(x+1,sz):
            if array[y] < array[base]:
                base = y
        array[base],array[x]=array[x],array[base]
    return array

if __name__ == '__main__':
    exp = random.sample(range(100),100)
    expect = [x for x in range(100)]
    rst = select_sort(exp)
    assert exp == expect
