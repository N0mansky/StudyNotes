import unittest
from base.datastructs import LinkNode
from base.datastructs import BinTree


def crt_links(start, end):
    head = LinkNode(start, None)
    curr = head
    for x in range(start + 1, end + 1):
        tmp = LinkNode(x, None)
        curr.pt = tmp
        curr = tmp
    return head


def crt_bintree():
    src = [5, 2, 8, 1, 3, 7, 9, 0, 4, 6, 10]
    mid = 5
    root = BinTree(mid, None, None)

    def insert(root, node):
        if node == root.val:
            return
        elif node < root.val:
            if root.left is not None:
                insert(root.left, node)
            else:
                root.left = BinTree(node, None, None)
        else:
            if root.right is not None:
                insert(root.right, node)
            else:
                root.right = BinTree(node, None, None)

    for val in src:
        insert(root, val)
    return root


class TestMethod(unittest.TestCase):

    def test_crt_bintree(self):
        root = crt_bintree()
        self.assertEqual(root.val, 5)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestMethod('test_crt_bintree'))
    unittest.TextTestRunner().run(suit)
