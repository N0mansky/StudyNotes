from base.datastructs import LinkNode


def crt_links(start, end):
    head = LinkNode(start, None)
    curr = head
    for x in range(start + 1, end + 1):
        tmp = LinkNode(x, None)
        curr.pt = tmp
        curr = tmp
    return head
