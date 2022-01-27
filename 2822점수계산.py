import sys


number_graph = [int(sys.stdin.readline())for _ in range(8)]
index_graph = [idx for idx in range(1,8+1)]
graph = list(map(lambda x,y: [y,x], number_graph, index_graph))


graph.sort(key = lambda x : x[1], reverse=True)
summation = 0
numbers = []

for idx in range(5):
    summation += graph[idx][1]
    numbers.append(graph[idx][0])

numbers.sort()
print(summation)
for idx in numbers:
    print(idx, end =' ')