import unittest

"""
Merging two ordered lists
"""


# loop and pop
def merge(l1, l2):
    tmp = []
    while l1 and l2:
        if l1[0] < l2[0]:
            tmp.append(l1.pop(0))
        else:
            tmp.append(l2.pop(0))
    while l1:
        tmp.append(l1.pop(0))
    while l2:
        tmp.append(l2.pop(0))
    return tmp


# tail-resursion
def recursion_merge_sort(l1,l2,tmp):
    if len(l1) ==0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    return recursion_merge_sort(l1,l2,tmp)




class TestMerge(unittest.TestCase):
    expected = [1, 10, 40, 55, 56, 57, 58, 66, 100, 100]

    def setUp(self):
        self.lista = [10, 57, 58, 66, 100]
        self.listb = [1, 40, 55, 56, 100]

    def test_merge(self):
        rst = merge(self.lista, self.listb)
        print(rst)
        self.assertEqual(rst, self.expected)

    def test_recursion_merge_sort(self):
        rst = []
        recursion_merge_sort(self.lista,self.listb,rst)
        print(rst)
        self.assertEqual(rst,self.expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
