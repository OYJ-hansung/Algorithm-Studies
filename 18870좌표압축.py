from operator import index
import sys

N = int(sys.stdin.readline())
index_list = []
for idx in range(N):
    index_list.append(idx)
graph = list(map(lambda x, y: [int(x), y], sys.stdin.readline().split(), index_list))
graph.sort()
temp = 10**10
temp_value = -1
for idx in range(N):
    if temp != graph[idx][0]:
        temp_value +=1
        graph[idx].extend([temp_value])
        temp = graph[idx][0]
    else:
        graph[idx].extend([temp_value])

graph.sort(key = lambda x: x[1])
for idx in graph:
    print(idx[2], end=' ')