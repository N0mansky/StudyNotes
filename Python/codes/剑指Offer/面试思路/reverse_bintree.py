"""
题目描述:操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树
    8
   /  \
  6   10
 / \  / \
5  7 9 11
镜像二叉树
    8
   /  \
  10   6
 / \  / \
11 9 7  5
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Resursive solution
"""


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


"""
Stack method
"""


class Solution2:
    def mirror(self, root):
        stx = [root]
        while len(stx) > 0:
            node = stx.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            if node.left:
                stx.append(node.left)
            if node.right:
                stx.append(node.right)
        return root


if __name__ == '__main__':
    pass
