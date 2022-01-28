import sys

N = int(sys.stdin.readline())
graph = [sys.stdin.readline().strip() for _ in range(N)]
graph.sort()
# print(graph)

temp = []
for serial in graph:
    summation = 0
    for idx in serial:
        if idx.isnumeric() == True:
            summation += int(idx)
    temp.append(summation)

graph_summation = list(map(lambda x, y: [x,y], temp, graph))
graph_summation.sort()
graph_summation.sort(key = lambda x: len(x[1]))
# print(graph_summation)

for serial in graph_summation:
    print(serial[1])

    