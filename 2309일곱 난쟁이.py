import sys

graph = [int(sys.stdin.readline()) for _ in range(9)]
graph.sort()
summation = sum(graph)
breakistrue = True

for idx in range(9):
    for i in range(9):
        if (summation - graph[idx] - graph[i]) == 100:
            a, b = graph[idx], graph[i]
            print(a, b)
            graph.remove(a)
            graph.remove(b) 
            breakistrue = False
            break
    if breakistrue == False:
        break

for idx in graph:
    print(idx)


    