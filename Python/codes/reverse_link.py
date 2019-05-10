import unittest
from utils.util import crt_links


def reverse_link(head):
    pre = head
    curr = head.pt
    pre.pt = None
    while curr:
        tmp = curr.pt   # Stored next nodes point
        curr.pt = pre  # Set previous nodes to current node's pt
        pre = curr     # Set curr node as previous node
        curr = tmp      # Set next node as current 
    return pre


class TestLink(unittest.TestCase):
    expect = [x for x in reversed(range(1, 11))]

    def setUp(self) -> None:
        self.head = crt_links(1, 10)

    def test_reverse_link(self):
        rst = []
        tmp = reverse_link(self.head)
        while tmp and tmp.val:
            rst.append(tmp.val)
            tmp = tmp.pt
        self.assertEqual(self.expect, rst)


if __name__ == '__main__':
    unittest.main()
