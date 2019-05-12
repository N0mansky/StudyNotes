# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 3:
            return number
        a, b = 1, 1
        for x in range(number):
            a, b = b, a + b
        return a


def abnormal_steps(n):
    if n < 2:
        return 1
    return abnormal_steps(n - 1) * 2


def jumpFloorII(number):
    if number < 2:
        return 1
    return pow(2, number - 1)


if __name__ == '__main__':
    print(abnormal_steps(4))
    print(jumpFloorII(4))
