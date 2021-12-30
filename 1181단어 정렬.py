import sys

N = int(sys.stdin.readline())
graph = [sys.stdin.readline().strip() for _ in range(N)]
graph.sort()
answer = list()

for idx in range(N):
    if [graph[idx], len(graph[idx])] not in answer:
        answer.append([graph[idx], len(graph[idx])])
    else:
        continue
answer.sort(key = lambda x : x[1])

for idx in answer:
    print(idx[0])