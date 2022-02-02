import sys

N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline().strip())for _ in range(N)]
graph.reverse()

answer = 0
max_num = graph[0]


for idx in range(1,N):
    if graph[idx] >= max_num:
        answer += (graph[idx]-max_num+1)
        graph[idx] = graph[idx] - (graph[idx]-max_num+1)
    max_num = graph[idx]

print(answer)

