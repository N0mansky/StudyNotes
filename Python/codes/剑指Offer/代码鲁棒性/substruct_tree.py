# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.is_subtree(pRoot1.left, pRoot2) or self.is_subtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, a_tree, b_tree):
        if not b_tree:
            return True
        if not a_tree or a_tree.val != b_tree.val:
            return False
        return self.is_subtree(a_tree.left, b_tree.left) and self.is_subtree(a_tree.right, b_tree.right)
