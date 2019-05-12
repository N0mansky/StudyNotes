""" 第一种方法：递归记忆法"""


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


"""第二种方法：循环法"""


def loop_fib(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
    return b


"""第三种方法：递归法"""


def fib_recur(n):
    if n <= 2:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


if __name__ == '__main__':
    # val = fib(10)
    # val = loop_fib(10)
    val = fib_recur(10)
    print(val)
