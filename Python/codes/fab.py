import unittest


"""The iterable class of fabonacci"""
class Fab(object):
    def __init__(self,max):
        self.n = 0
        self.a = 0
        self.b = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            self.a,self.b = self.b,self.a+self.b
            self.n += 1
            return self.a
        raise StopIteration('Done')

"""The generator of fabonacci"""
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        a,b = b, a+b
        n+=1
        yield a

class TestFab(unittest.TestCase):

    expect = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_fab(self):
        gen = fab(10)
        data = [ x for x in gen]
        self.assertEqual(data,self.expect)

    def test_fab_class(self):
        gen = Fab(10)
        data = [ x for x in gen]
        self.assertEqual(data,self.expect)

if __name__ == '__main__':
    unittest.main()
