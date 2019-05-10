import unittest

"""
This module is determine two words anagram
"""
# Two layers loop
def solution1(s1,s2):
    s2 = list(s2)
    ls1 = len(s1)
    ls2 = len(s2)
    if ls1 != ls2:
        return False
    for x in s1:
        found = False
        for i in range(ls2):
            if x == s2[i]:
                s2[i] = None
                break
        else:
            return False
    return True

# Sorted method
def solution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = len(alist1) if len(alist1) > len(alist2) else len(alist2)
    for x in range(pos):
        if alist1[x] != alist2[x]:
            return False
    return True

# iterator method
def solution3(s1,s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for x in s1:
        c1[ord(x) - 97] +=1
    for x in s2:
        c2[ord(x) - 97] +=1
    if c1 == c2:
        return True
    else:
        return False

class TestAnagram(unittest.TestCase):
    data1 = ['abcd', 'army', 'bcdaa','bcdaaa']
    data2 = ['dcba', 'mary', 'bcdaaa','bcdaa']
    expect = [True, True, False,False]

    def test_solution1(self):
        rst = []
        for x in range(len(self.data1)):
            rst.append(solution1(self.data1[x], self.data2[x]))
        self.assertEqual(rst, self.expect)

    def test_solution2(self):
        rst = []
        for x in range(len(self.data1)):
            rst.append(solution2(self.data1[x], self.data2[x]))
        self.assertEqual(rst, self.expect)

    def test_solution3(self):
        rst = []
        for x in range(len(self.data1)):
            rst.append(solution3(self.data1[x], self.data2[x]))
        self.assertEqual(rst, self.expect)

if __name__ == '__main__':
    unittest.main()
