import unittest
import random

"""
All sorts method
"""


# Recursive quicksort
def recur_quicksort(item, left, right):
    if left > right:
        return
    base = item[left]
    i, j = left, right
    while i != j:
        while item[j] >= base and i < j:
            j -= 1
        while item[i] <= base and i < j:
            i += 1
        if i < j:
            item[i], item[j] = item[j], item[i]
    item[left] = item[i]
    item[i] = base
    recur_quicksort(item, left, i - 1)
    recur_quicksort(item, i + 1, right)

# loop Quick sort
def quick_sort():
    pass


class TestSort(unittest.TestCase):
    expected = [x for x in range(100)]

    def setUp(self):
        self.item = random.sample(range(100), 100)

    def test_recur_quicksort(self):
        recur_quicksort(self.item, 0, len(self.item) - 1)
        self.assertEqual(self.item, self.expected)

    def test_quick_sort(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=3)
