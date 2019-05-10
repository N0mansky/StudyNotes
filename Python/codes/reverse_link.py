import unittest
from utils.util import crt_links


def reverse_link(head):
    nx = head.pt
    head.pt = None
    while nx:
        tmp = nx.pt
        nx.pt = head
        head = nx
        nx = tmp
    return head


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
