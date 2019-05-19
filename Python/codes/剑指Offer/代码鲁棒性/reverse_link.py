from utils.util import crt_links

"""
Reversing link
原题:输入一个链表，反转链表后，输出新链表的表头。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, val=None,next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        prev = pHead
        if not prev:
            return
        curr = prev.next
        prev.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


if __name__ == '__main__':
    lhead = crt_links(1, 10)
    s = Solution()
    rst = s.ReverseList(lhead)
    print(rst.val)
