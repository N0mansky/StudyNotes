"""
题目描述:
1.后序遍历二叉树
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路: 该道题的意思是需要判断这个序列是给出的后续遍历的结果,需要判断该结果是否符合二叉树的结构,
二叉树的结构:
1. 节点左边的值都比二叉树
2. 节点右边的值都比二叉树大

所以首先找到根节点,根节点肯定是最后一个元素,然后不断的递归判断左子树和右子树是否符合规则
"""

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        s_len = len(sequence)
        if s_len == 1:
            return True
        root = sequence[-1]
        for l in range(s_len):
            if sequence[l] > root:
                break
        for r in range(l, s_len):
            if sequence[r] < root:
                return False
        left = right = True
        if l > 0:
            left = self.VerifySquenceOfBST(sequence[:l])
        if l < s_len - 1 and left:
            right = self.VerifySquenceOfBST(sequence[l:-1])
        return left and right
