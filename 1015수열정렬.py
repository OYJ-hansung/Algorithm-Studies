import sys
N = int(sys.stdin.readline())
idx = 0
idx_list = []
graph = list(enumerate(list(map(int, sys.stdin.readline().split()))))
graph_sorted = sorted(graph, key = lambda x: x[1])

for i in range(N):
    idx_list.append(idx)
    idx +=1

graph_sorted = list(map(lambda x, y: [x, y], graph_sorted, idx_list))
graph_sorted.sort(key=lambda x: x[0][0])
for idx in graph_sorted:
    print(idx[1], end=' ')