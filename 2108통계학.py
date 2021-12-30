import sys

N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline()) for _ in range(N)]
graph.sort()
summation = sum(graph)
middle_index = ((len(graph) - 1) // 2)
max_count = 0
counts = 0

for idx in range(len(graph)):
    if max_count < graph.count(graph[idx]):
        max_count = graph.count(graph[idx])
    else:
        counts +=1
    graph[idx] = [graph[idx], graph.count(graph[idx])]

mid = graph[middle_index][0]
graph.sort(key = lambda x: x[1], reverse=True)

if counts == 1:
    max_count_num = graph[-1][0]
    print('counts', counts)
else:
    print('counts', counts)
    max_count_num = graph[-1][0]

print(format(summation//N, '.0f'))
print(mid)
print(max_count_num)
print(graph[-1][0] - graph[0][0])