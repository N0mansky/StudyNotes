import unittest
from utils.util import crt_links


def node(l1, l2):
    length1, length2 = 0, 0
    a, b = l1, l2
    while l1.pt:
        length1 += 1
        l1 = l1.pt
    while l2.pt:
        length2 += 1
        l2 = l2.pt

    if length1 > length2:
        for _ in range(length1 - length2):
            a = a.pt
    else:
        for _ in range(length2 - length1):
            b = b.pt
    while a and b:
        if a.pt == b.pt:
            return a.pt
        else:
            a = a.pt
            b = b.pt


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.expected = crt_links(5, 8)
        self.head1 = crt_links(1, 4)
        self.head2 = crt_links(3, 4)
        l1 = self.head1
        l2 = self.head2
        while l1.pt:
            l1 = l1.pt
        while l2.pt:
            l2 = l2.pt
        l1.pt = self.expected
        l2.pt = self.expected

    def test_node(self):
        rst = node(self.head1, self.head2)
        self.assertEqual(rst, self.expected)


if __name__ == '__main__':
    unittest.main()
