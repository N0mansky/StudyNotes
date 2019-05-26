# coding=utf-8
"""
# 字符串的排列

## 题目描述:

> 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
> 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串
> abc,acb,bac,bca,cab和cba。

## 思路:
1. 使用回溯算法,固定第一个字母,然后不断递归子串,递归完成后,切换第一个固定的首字母
2. 分解总的来说,就是大事不断话小,不断变成子问题,然后调用递归
"""

"""
直接使用内部的permutation方法
"""
# 导入itertools
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        # 如果输入的字符串为空,则返回空集合
        if ss == "":
            return []
        # 计算组合的种类
        lst = list(itertools.permutations(list(ss)))
        # 去重并连接字符
        result = []
        for el in lst:
            x = "".join(el)
            if x not in result:
                result.append(x)

        return result
"""
递归
"""
class Solution2:
    def Permutation(self, ss):
        # write code here
        # 如果ss为空,返回空集合
        if not ss:
            return []
        # 创建一个set
        result_set = set([])
        # 定义递归方法,传入一个ss的list,和当前的字符
        def permutation(cs, current_s):
            # 如果当前的list为空,则把当前的字符加入到结果集里面,并返回
            if not cs:
                # set 自动去重
                result_set.add(current_s)
                return
            # 否则的话,不断的递归list里面的字符
            for index, c in enumerate(cs):
                # 创建一个当前字符后加1的新的list
                new_cs = [char for i, char in enumerate(cs) if index != i]
                # 递归该list,并把传入的字符加上之前的current_s
                permutation(new_cs, current_s+cs[index])
            return
        permutation([c for c in ss], "")
        # 对结果进行排序
        return sorted(list(result_set))
