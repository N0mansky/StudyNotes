import unittest

"""
All search algorithm
"""


def binsearch(key, item):
    length = len(item)
    lo, hi = 0, length - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        if item[mid] == key:
            return mid
        elif item[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.item = [x for x in range(100)]
        self.expect = [0, None, 87, 88, 99]

    def test_binsearch(self):
        v1 = binsearch(0, self.item)
        v2 = binsearch(100, self.item)
        v3 = binsearch(87, self.item)
        v4 = binsearch(88, self.item)
        v5 = binsearch(99, self.item)
        rst = [v1, v2, v3, v4, v5]
        self.assertEqual(rst, self.expect)


if __name__ == '__main__':
    unittest.main()
