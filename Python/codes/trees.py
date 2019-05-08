import copy
import unittest
from base.datastructs import BinTree

from utils.util import crt_bintree

"""
Iterating tree
"""


# BFS
def wide_first(root):
    rst = []
    queue = [root]
    while queue:
        if queue[0].left is not None:
            queue.append(queue[0].left)
        if queue[0].right is not None:
            queue.append(queue[0].right)

        rst.append(queue[0].val)
        queue.pop(0)
    return rst


# BFS2
def wide_first2(root, rst=[]):
    row = [root]
    while row:
        for x in row:
            rst.append(x.val)
        row = [kid for item in row for kid in (item.left, item.right) if kid]


# DFS
def pre_traverse(root, rst=None):
    if root:
        rst.append(root.val)
        pre_traverse(root.left, rst)
        pre_traverse(root.right, rst)


def mid_traverse(root, rst=None):
    if root:
        mid_traverse(root.left, rst)
        rst.append(root.val)
        mid_traverse(root.right, rst)


def post_traverse(root, rst=None):
    if root:
        post_traverse(root.left, rst)
        post_traverse(root.right, rst)
        rst.append(root.val)


# Get the max deep of tree
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


# Determine two tree equality
def sametree(p, q):
    if p and q:
        if p.val == q.val:
            left_rst = sametree(p.left, q.left)
            if not left_rst:
                return left_rst
            right_rst = sametree(p.right, q.right)
            if not right_rst:
                return right_rst
            return left_rst and right_rst
        else:
            return False
    elif p is None and q is None:
        return True
    else:
        return False


def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False


# Get the post_traverse by pre_traverse and mid_traverse
# First need rebuild tree,then execute post_traverse
def rebuild(pre, mid):
    if not pre:
        return None
    head = BinTree(pre.pop(0), None, None)
    idx = mid.index(head.val)
    if len(mid[:idx]) > 0:
        head.left = rebuild(pre, mid[:idx])
    if len(mid[idx + 1:]) > 0:
        head.right = rebuild(pre, mid[idx + 1:])
    return head


class TestTree(unittest.TestCase):
    root = crt_bintree()

    def test_wide_first(self):
        expect = [5, 2, 8, 1, 3, 7, 9, 0, 4, 6, 10]
        rst = wide_first(self.root)
        rst2 = []
        wide_first2(self.root, rst2)
        self.assertEqual(rst, rst2, expect)

    def test_deep_first(self):
        pre_expect = [5, 2, 1, 0, 3, 4, 8, 7, 6, 9, 10]
        mid_expect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        post_expect = [0, 1, 4, 3, 2, 6, 7, 10, 9, 8, 5]

        pre_rst = []
        mid_rst = []
        post_rst = []

        pre_traverse(self.root, pre_rst)
        mid_traverse(self.root, mid_rst)
        post_traverse(self.root, post_rst)

        self.assertEqual(pre_rst, pre_expect)
        self.assertEqual(mid_rst, mid_expect)
        self.assertEqual(post_rst, post_expect)

    def test_maxdepth(self):
        expect = 4
        self.assertEqual(maxDepth(self.root), expect)

    def test_sametree(self):
        q = copy.deepcopy(self.root)
        q2 = copy.deepcopy(self.root)
        q2.right.right.val = -1

        rst = sametree(q, self.root)
        rst2 = sametree(q2, self.root)

        sa = isSameTree(q, self.root)
        sa2 = isSameTree(q2, self.root)

        self.assertTrue(rst)
        self.assertTrue(sa)
        self.assertFalse(sa2)
        self.assertFalse(rst2)

    def test_rebuild(self):
        pre = [5, 2, 1, 0, 3, 4, 8, 7, 6, 9, 10]
        mid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        post_expect = [0, 1, 4, 3, 2, 6, 7, 10, 9, 8, 5]
        head = rebuild(pre, mid)

        post_rst = []
        post_traverse(head, post_rst)
        self.assertEqual(post_rst, post_expect)


if __name__ == '__main__':
    unittest.main()
