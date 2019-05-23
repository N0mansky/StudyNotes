"""
题目描述:从上往下,从左往右打印每个二叉树的节点
思路:BFS广度优先,使用队列存储节点
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code herep
        if not root:
            return []
        q = [root]
        rst = []
        while len(q)> 0:
            node = q.pop(0)
            rst.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return rst
