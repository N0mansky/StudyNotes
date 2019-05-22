"""
题目描述:
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = [pushV[0]]
        l_push = len(pushV)
        l_pop = len(popV)
        rst = False
        if l_push != l_pop:
            return rst
        i = 0
        j = 1
        while i < l_pop:
            if stack[-1] != popV[i]:
                if j >= l_push:
                    break
                stack.append(pushV[j])
                j += 1
            else:
                stack.pop()
                i += 1
        if not stack:
            rst = True
        return rst


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 3, 2, 1]
    s = Solution()
    print(s.IsPopOrder(a, b))
    b = [4, 3, 5, 1, 2]
    print(s.IsPopOrder(a, b))
