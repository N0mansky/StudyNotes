class LinkNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        rst = ''
        while self:
            rst += str(self.val)
            rst += '->'
            self = self.next
        rst += 'None'
        return rst


class BinTree(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
