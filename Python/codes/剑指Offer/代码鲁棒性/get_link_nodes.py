from utils.util import crt_links

"""
Get the specified count backward link node
原题:输入一个链表，输出该链表中倒数第k个结点。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.pt = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k < 1:
            return
        pt_1 = pt_2 = head
        k = k - 1
        while pt_1.pt and k > 0:
            pt_1 = pt_1.pt
            k -= 1
        if k > 0:
            return
        while pt_1.pt:
            pt_1 = pt_1.pt
            pt_2 = pt_2.pt
        return pt_2


if __name__ == '__main__':
    data = crt_links(1, 10)
    s = Solution()
    rst = s.FindKthToTail(data, 5)
    print(rst.val)
