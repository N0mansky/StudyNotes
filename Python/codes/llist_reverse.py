import unittest
"""
Reversing one-way link-list
e.g.,1->2->3->4 reversed to 2->1->4->3
"""
class LinkNode(object):
    def __init__(self,val,pt):
        self.val = val
        self.pt = pt


def pair_rev(head):
    if head is None: return
    curr = head
    while curr is not None:
        if curr.pt is not None:
            curr.val,curr.pt.val = curr.pt.val,curr.val
            curr = curr.pt.pt
        else:
            break

class TestLink(unittest.TestCase):

    expected1 = [2,1,4,3,5]
    expected2 = [2,1,4,3,6,5]

    def setUp(self):
        self.head1 = self.crt_links(1,5)
        self.head2 = self.crt_links(1,6)

    def test_pair_rev(self):
        pair_rev(self.head1)
        pair_rev(self.head2)
        rst1=self.prt_link(self.head1)
        rst2=self.prt_link(self.head2)
        self.assertEqual(rst1,self.expected1)
        self.assertEqual(rst2,self.expected2)

    @staticmethod
    def prt_link(head):
        l = []
        curr = head
        while curr is not None and curr.val:
            l.append(curr.val)
            curr = curr.pt
        print(l)
        return l

    @staticmethod
    def crt_links(start,end):
        head = LinkNode(start,None)
        curr = head
        for x in range(start+1,end+1):
            tmp = LinkNode(x,None)
            curr.pt = tmp
            curr = tmp
        return head

if __name__ == '__main__':
    unittest.main()
