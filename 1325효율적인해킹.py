import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(N+1)]

for idx in range(M):
    com1, com2 = map(int, sys.stdin.readline().split())
    graph[com2].append(com1)


def DFS(graph, start):
    global answer

    visited = [False]*(N+1)
    visited[start] = True
    for idx in graph[start]:
        if not visited[idx]:
            DFS(graph, idx)
            answer +=1

def BFS(graph, start):
    answer = 0
    visited = [False]*(N+1)
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        next = q.popleft()
        for idx in graph[next]:
            if not visited[idx]:
                visited[idx]=True
                q.append(idx)
                answer+=1
    return answer
    
answer_list = []
max_answer = -1
for start in range(1, N+1):
    answer = BFS(graph, start)
    max_answer = max(max_answer, answer)
    if answer !=max_answer:
        continue
    else:
        answer_list.append([start, answer])

for a, b in answer_list:
    if b == max_answer:
        print(a, end=' ')