import sys
from collections import deque


def BFS(x, y):
        visited[x][y] = True
        q = deque()
        q.append([x, y])

        while q:
            x, y = q.popleft()
            for dx, dy in [[-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2]]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny]==0:
                    if nx == target_x and ny == target_y:
                        answer_list[idx].append(graph[x][y]+1)
                    else:
                        visited[nx][ny] = True
                        graph[nx][ny] = graph[x][y] +1
                        q.append([nx, ny])

T = int(sys.stdin.readline())
gather_answer = []
answer_list = [[]for _ in range(T)]
for idx in range(T):  
    N = int(sys.stdin.readline())
    graph = [[0 for _ in range(N)]for _ in range(N)]
    knight_x, knight_y = list(map(int, sys.stdin.readline().split()))
    target_x, target_y = list(map(int, sys.stdin.readline().split()))
    visited = [[False for _ in range(N)]for  _ in range(N)]
    BFS(knight_x, knight_y)

for answer in answer_list:
    if len(answer) == 0:
        print(0)
    else:
        print(min(answer))
    

    
            
                



