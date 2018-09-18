#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
基础编程题
pos为二元序对(i,j)

"""


def read_region(f):
    region = []
    for line in f:
        clean_line  = line.strip()
        region.append(list(clean_line))
    return region


def mark_island(region, i, j):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if len(region) > i >= 0 and len(region[0]) > j >= 0:
        if region[i][j] == '1':
            region[i][j] = '2'  # 对当前陆地进行标记
            # print("=============标记了一片陆地=============")
            for fx in range(4):
                next_i = i + dirs[fx][0]
                next_j = j + dirs[fx][1]
                mark_island(region, next_i, next_j)
    return region


def count_island(region):
    num_islands = 0
    i = 0
    while i < len(region):
        j = 0
        while j < len(region[0]):
            if region[i][j] == '1':
                region = mark_island(region, i, j)
                num_islands += 1
                j += 1
            else:
                j += 1
        i += 1
    return num_islands


if __name__ == '__main__':
    ISLANDS_FILE = 'E:/IT_ZIYAN/GUANGZHOU_MISSION/MISSION_0913_AM/islands.txt'

    with open(ISLANDS_FILE, 'r') as many_f:
        regions = []
        region = []
        for line in many_f:
            if line.strip() != '---':
                region.append(line.strip())
            else:
                regions.append(region)
                region = []
                continue

        for item in regions:
            region = read_region(item)
            print(count_island(region))
