def find(key,array):
    h = len(array) -1
    w = len(array[0] -1) -1
    raw,col = 0,w
    while h >= raw and col >= 0:
        val = array[raw][col]
        if val == key:
            return raw,col
        elif key >  val:
            raw += 1
        elif key < val:
            col -= 1
    return None
