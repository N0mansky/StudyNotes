"""
# 归并排序
## 思想:
1. 把两个有序的序列逐个对比,最终可以合并这两个有序成一个有序序列
2. 不断划分问题为子问题,使用递归不断划分成子问题,最后合并
3. 分治法
"""
import random

"""
non-in-place写法
因为创建了新的list
time-complexity:O(nlogn)
space-complexity:O(n)
"""
def merge_sort(array):
    rst = []
    a_len = len(array)
    if a_len < 2:
        return array
    mid = a_len // 2
    rst_left=merge_sort(array[:mid])
    rst_right=merge_sort(array[mid:])
    while rst_left and rst_right:
        if rst_left[0] < rst_right[0]:
            rst.append(rst_left.pop(0))
        else:
            rst.append(rst_right.pop(0))
    rst.extend(rst_left)
    rst.extend(rst_right)
    return rst

if __name__ == '__main__':
    exp = random.sample(range(100),100)
    expected = [x for x in range(100)]
    rst =merge_sort(exp)
    assert rst == expected




