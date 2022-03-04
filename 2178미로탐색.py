import sys
from collections import deque
from pprint import pprint
row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(row)]

def BFS1(x, y):
    global answer
    visited = [[False for _ in range(col)]for _ in range(row)]
    visited[x][y] = True
    q = deque()
    q.append([x, y])

    while q:
        a, b = q.popleft()

        if a == (row-1) and b==(col-1):
            pprint(visited)
            print()
            return True

        for dx, dy in [[1,0],[0, 1],[-1, 0],[0,-1]]: # down, right, up
            nx = a + dx
            ny = b + dy
            if 0<=nx<row and 0<=ny<col:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                        answer +=1
                        visited[nx][ny] = True
                        q.append([nx, ny])
                        break
    return False

def BFS2(x, y):
    global answer
    visited = [[False for _ in range(col)]for _ in range(row)]
    visited[x][y] = True
    q = deque()
    q.append([x, y])

    while q:
        a, b = q.popleft()

        if a == (row-1) and b==(col-1):
            pprint(visited)
            return True

        for dx, dy in [[0, 1],[1,0],[-1, 0],[0,-1]]: # right, down, up
            nx = a + dx
            ny = b + dy
            if 0<=nx<row and 0<=ny<col:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                        answer +=1
                        visited[nx][ny] = True
                        q.append([nx, ny])
                        break
    return False
    
min_answer = (row*col)
answer = 1
if BFS1(0,0):
    min_answer = min(answer, min_answer)

answer = 1
if BFS2(0,0):
    min_answer = min(answer, min_answer)
print(min_answer)
pprint(graph)