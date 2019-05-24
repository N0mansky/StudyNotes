"""
## 快速排序

### 思路:
1. 快速排序也是用的是分治算法的思想,核心思路是:
    - 从数组中拿一个元素作为参照
    - 确保该元素左边的元素都小于该元素
    - 确保该元素右边的元素都大于该元素
    - 如果左边的序列或者右边的序列大于3个,则需要再次重复上述步骤继续划分
    - 直到左边的序列和右边的序列都有序,那么整个序列就有序了
2. 通常情况下,选取pivot一般是左边第一个元素,那么哨兵开始前进需要从右边开始走
3 .假设序列如下:[6,1,2,7,9]
如果左边开始先走,那么最后i肯定是停留在7的位置,然后右边开始走,也停留在7的位置,然后结束循环,
在最后的交换pivot后,6和7交换了,那么结果是错误的
4. 如果是右边先走,那么最后的停留位置就是2,然后交换pivot就是正确的,所以右边先走可以保证相遇的元素
一定是小于pivot的
### 复杂度:
1. Time-complexity:O(nlogN)
2. Space-complexity:O(n)
3. In-place算法
"""
import random


def recur_quick(array, left, right):
    # 如果左边的下标大于右边的,则返回
    if left > right:
        return
    # 将数组的0个元素设置为参照元素,设置两个index当做哨兵,变量分别从数组的1和尾部出发
    consult = array[left]
    i,j =left,right
    # 如果i和j相遇了,则终止循环
    while i != j:
        # 下标j的元素如果小于consult,则停止递减
        while array[j] >= consult and i < j:
            j -= 1
        # 下标i的元素如果大于consult,则停止递增
        while array[i] <= consult and i < j:
            i += 1
        # 交换i,j的元素
        if i < j:
            array[i], array[j] = array[j], array[i]
    # 交换参照元素
    array[i], array[left] = consult, array[i]
    recur_quick(array, left, i - 1)
    recur_quick(array, i + 1, right)


if __name__ == '__main__':
    exp = random.sample(range(100), 100)
    print(exp)
    recur_quick(exp, 0, 99)
    print(exp)
