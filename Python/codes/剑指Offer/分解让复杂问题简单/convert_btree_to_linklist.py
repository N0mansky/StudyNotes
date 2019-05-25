"""
二叉搜索树与双向链表
题目描述:
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
思路1:
1. 因为要求是排序的,所以使用中序遍历,并放到一个list中
2. 然后遍历修改指针

思路2:
1. 使用中序排序,那么对于root节点,所有的左子节点都是root节点的前驱,所有的右节点都是root节点的后继
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    l = []
    def Convert(self, pRootOfTree):
        # write code here
        def get_list(root):
            if not root:
                return
            get_list(root.left)
            self.l.append(root)
            get_list(root.right)

        get_list(pRootOfTree)

        l_len = len(self.l)
        if l_len == 0:
            return
        self.l[0].left=None
        if l_len < 2:
            self.l[0].right = None
        else:
            self.l[0].right=self.l[1]
            for x in range(1,l_len-1):
               self.l[x].left = self.l[x-1]
               self.l[x].right = self.l[x+1]
            self.l[-1].left = self.l[-2]
            self.l[-1].right = None
        head = self.l[0]
        del self.l[:]
        return head

class Solution2:
    def Convert(self, pRootOfTree):
        # write code here
        # 如果节点为空,那么说明是空树
        if not pRootOfTree:
            return pRootOfTree
        # 如果节点的左子树和右子树都没有,那么说明是叶子节点,返回该节点
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 不断递归左子树
        self.Convert(pRootOfTree.left)
        # 获取左子树节点
        left = pRootOfTree.left
        # 如果左子树的存在,且该节点存在右节点,连接根与左子树的最大节点
        if left:
            while left.right:
                left = left.right
            left.right = pRootOfTree
            pRootOfTree.left = left

        # 不断递归右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        # 若右子树存在,连接根与右子树的最小节点
        if right:
            while right.left:
                right = right.left
            right.left = pRootOfTree
            pRootOfTree.right = right

        # 从root节点不断往head方向移动,获取头节点
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
