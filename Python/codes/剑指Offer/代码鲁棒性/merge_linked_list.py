from base.datastructs import LinkNode
from utils.util import crt_links

"""
题目描述:输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        rst_head = LinkNode('tmp_head')
        tmp_head = rst_head
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                tmp_head.next = pHead1
                pHead1 = pHead1.next
            else:
                tmp_head.next = pHead2
                pHead2 = pHead2.next
            tmp_head = tmp_head.next
        if pHead1:
            tmp_head.next = pHead1
        if pHead2:
            tmp_head.next = pHead2
        rst_head = rst_head.next
        return rst_head


if __name__ == '__main__':
    s = Solution()
    pHead1 = crt_links(1, 10)
    print(pHead1)
    pHead2 = crt_links(7, 11)
    print(pHead2)
    rst = s.Merge(pHead2, pHead1)
    print(rst)
