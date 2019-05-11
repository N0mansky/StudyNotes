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


def minNumberInRotateArray(rotateArray):
    l = rotateArray
    length = len(l)
    if l == 0:
        return 0
    left, right = 0, length - 1
    while l[left] >= l[right]:
        if right - left == 1:
            return l[right]
        mid = (left + right) // 2
        if l[mid] > l[left]:
            left = mid
        if l[mid] < l[right]:
            right = mid
    return l[mid]


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

    def test_minNumberInRotateArray(self):
        test_data = [6501, 6828, 6963, 7036, 7422, 7674, 8146, 8468, 8704, 8717, 9170, 9359, 9719, 9895, 9896,
                     9913, 9962, 154, 293, 334, 492, 1323, 1479, 1539, 1727, 1870, 1943, 2383, 2392, 2996, 3282,
                     3812, 3903, 4465, 4605, 4665, 4772, 4828, 5142, 5437, 5448, 5668, 5706, 5725, 6300, 6335]
        print(minNumberInRotateArray(test_data))



if __name__ == '__main__':
    unittest.main()
