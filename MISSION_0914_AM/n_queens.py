#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
8皇后问题

"""
import pandas as pd


def init_maze_n(n):
    hang = ['0' for i in range(n)]
    maze_n = []
    for i in range(n):
        maze_n.append(hang)
    maze = pd.DataFrame(maze_n)
    return maze


def mark_q(maze, i, j):
    maze[i][j] = 'Q'

    n = len(maze[0])
    for hbl in range(n):
        if maze[i][hbl] == '0':
            maze[i][hbl] = 'N'
    for lbl in range(n):
        if maze[lbl][j] == '0':
            maze[lbl][j] = 'N'
    for x in range(n):
        for y in range(n):
            if abs(x - i) == abs(y - j) and x != i and y != j:
                if maze[x][y] == '0':
                    maze[x][y] = 'N'

    return maze


def gtr(maze, lie_ix):
    n = len(maze[0])

    for j in range(n):
        if maze[lie_ix][j] == '0':
            maze_copy = maze.copy()
            yield mark_q(maze_copy, lie_ix, j)


def exist_zero(maze):
    n = len(maze[0])
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '0':
                return True
    else:
        return False


def n_qreen(maze, current_N, cnt=[]):
    n = len(maze[0])
    if exist_zero(maze):
        for item in gtr(maze, current_N):
            n_qreen(item, current_N + 1)
    else:
        if current_N == n:
            cnt.append('suanzi')
            print(maze)
            print('-'*40)
    return len(cnt)


if __name__ == '__main__':
    n = 8
    maze = init_maze_n(n)
    ans = n_qreen(maze, 0)
    print('='*50)
    print("{}皇后问题解共计{}种".format(n, ans))
