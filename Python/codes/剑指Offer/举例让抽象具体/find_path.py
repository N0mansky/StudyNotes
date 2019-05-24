"""
题目描述:
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
思路:其实这道题考的就是DFS
Python version:2.7.3
"""


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        rst = []
        if not root:
            return rst

        def find(root, path, curr_num):
            if not root:
                return
            curr_num += root.val
            path.append(root.val)
            is_leaf = not (root.left or root.right)
            if curr_num == expectNumber and is_leaf:
                rst.append(path[:])
            find(root.left, path, curr_num)
            find(root.right, path, curr_num)
            # 深度遍历完一条路径后,需要回退
            path.pop()

        find(root, [], 0)
        return rst
