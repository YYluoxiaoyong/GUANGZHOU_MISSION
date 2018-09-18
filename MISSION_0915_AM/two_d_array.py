#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
测试二维列表的可变情况

"""

a = [[15, 15], [15, 15]]
print(a)
a[0][1] = 100
print(a)
print(id(a[0]), id(a[1]))
# ########################################代码段一


def init_maze_n(n):
    hang = [15 for i in range(n)]
    maze_n = []
    for i in range(n):
        maze_n.append(hang)
    return maze_n


b = init_maze_n(2)
print(b)
b[0][1] = 100
print(b)
print(id(b[0]), id(b[1]))
# ########################################代码段二
