import sys

N, tape = map(int, sys.stdin.readline().split())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()
answer = 1
covered = graph[0] + (tape -1)

for idx in range(1, N):
    if graph[idx] <= covered:
        continue
    else:
        covered = graph[idx] + (tape -1)
        answer +=1
print(answer)
    