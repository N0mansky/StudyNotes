"""
题目描述:定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self,stack=[],min_ele=[]):
        self.stack = stack
        self.min_ele = min_ele
    def push(self, node):
        # write code here
        if not self.stack:
            self.min_ele.append(node)
        elif node <= self.min_ele[-1]:
            self.min_ele.append(node)
        else:
            self.min_ele.append(self.min_ele[-1])
        self.stack.append(node)
    def pop(self):
        # write code here
        self.min_ele.pop()
        return self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_ele[-1]

if __name__ == '__main__':
    s = Solution()
    for x in range(5,0,-1):
        s.push(x)

    print(s.min())
    while s.stack:
        print(s.pop())

