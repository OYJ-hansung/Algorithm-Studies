import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
graph.sort()

graph.sort(key = lambda x : x[1])

answer = 1
end = graph[0][1]
for start in graph:
    if start[0] >= end:
        answer +=1
        end = start[1]

print(answer)