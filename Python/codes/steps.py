# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 3:
            return number
        a,b = 1,1
        for x in range(number):
            a,b = b,a+b
        return a 
