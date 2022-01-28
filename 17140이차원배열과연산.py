from collections import Counter
from functools import reduce
import sys

target_row, target_col, target_num = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(3)]

def R(graph):
    max_len = 0
    new_graph = []
    for row in graph:
        row_counter = Counter(row)
        del row_counter[0]
        row_count_list = list(row_counter.items())
        row_count_list.sort(key = lambda x: (x[1], x[0]))
        if len(row_count_list) > 50:
            row_count_list = row_count_list[:50]
        row_count_reduced = reduce(lambda x, y : list(x)+list(y), row_count_list[1:], list(row_count_list[0]))
        new_graph.append(row_count_reduced)
        max_len = max(max_len, len(row_count_reduced))

    for row in new_graph:
        if len(row) < max_len:
            row.extend([0]*(max_len-len(row)))
            
    return new_graph

time = 0
while True:
    if (target_row-1) < len(graph) and (target_col-1) < len(graph[0]):
        if graph[target_row-1][target_col-1] == target_num:
            print(time)
            break
    if time >100:
        print(-1)
        break

    if len(graph) >= len(graph[0]):
        graph = R(graph)
    else:
        graph = list(map(list,zip(*graph)))
        graph = R(graph)
        graph = list(map(list,zip(*graph)))
    time +=1

    

