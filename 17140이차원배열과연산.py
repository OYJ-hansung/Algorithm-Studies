from itertools import count
import sys
from bisect import bisect_left, bisect_right
from pprint import pprint
from unittest.util import _count_diff_hashable
target_row, target_col, target_value = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
pprint(graph, width=20)

def countNum(num, row):
    a, b = bisect_left(row, num), bisect_right(row, num)
    return b-a




temp = []
while graph[target_row-1][target_col] != target_value:
    for row in graph:
        length = len(row) # 3
        row.sort()
        row_set = sorted(set(row)) # [1, 1, 2]
        for idx in row_set:
            temp.append([idx,countNum(idx, row)]) # [[1, 2], [2, 1]]
        temp.sort(key=lambda x: x[0])
        temp.sort(key=lambda x: x[1]) # [[2, 1][1, 2]]
        print(temp)
    break



