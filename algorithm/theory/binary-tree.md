## 二叉查找树的插入
TREE-INSERT(T,z) 在二叉树T中插入变量z
1. 声明一个空变量y
2. 将root节点赋值给var x
3. loop:如果x不为空：
4.      将x赋值给y 
5.      如果: z的值 < x的值
6.            then:将 x的左树赋值给x
7.            else:将 x的右树赋值给x
8. 将y的引用(即遍历出来的合适的位置)赋值给z的父引用
9. if y 等于空
10.     then: 将 z设置为根节点 
11. else if z的值 < y的值:
        then: 将z赋值给 y 的左树
        else: 将z赋值给 y的右树
