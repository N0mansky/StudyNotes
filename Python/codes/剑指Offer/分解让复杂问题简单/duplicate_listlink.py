"""
复杂链表的复制
题目描述:
输入一个复杂链表
（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
思路:
1. 新节点复制旧链表的节点值,先不管引用然后插入原链表,如:
    old:  A->B->C
    new:  A->A1->B->B1-C-C1
2. 设置新节点的random指针的值
    A1.random = A.random.next
3. 并切分两个链表:
    A.next = A.next.next
    A1.next = A1.next.next

"""
from base.datastructs import RandomListNode
from utils.util import crt_random_linklist


# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        curr = pHead
        while curr:
            new = RandomListNode(curr.label)
            next = curr.next
            curr.next = new
            new.next = next
            curr = next

        curr = pHead
        while curr:
            new_node = curr.next
            if curr.random:
                new_node.random = curr.random.next
            curr = new_node.next

        new_head = pHead.next
        curr = pHead
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            else:
                new_node.next = None
            curr = curr.next
        return new_head


if __name__ == '__main__':
    head1 = crt_random_linklist(1, 10)
    print(head1)
    s = Solution()
    head2 = s.Clone(head1)
    print(head2)
