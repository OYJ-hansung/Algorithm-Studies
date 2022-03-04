from copy import deepcopy
import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
graph_original = [list(sys.stdin.readline().strip())for _ in range(row)]
white_board = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
black_board = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]



def BFS(a, b, graph, board):
    answer = 0
    visited = [[False for _ in range(col)]for _ in range(row)]
    visited[a][b] = True
    if (board[0][0] != graph[a][b]):
        answer +=1
    q = deque()
    q.append([a, b])
    
    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if a<=nx<(a+8) and b<=ny<(b+8):
                # print(nx, ny)
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    if (board[nx-a][ny-b] != graph[nx][ny]):
                        answer +=1
    return answer

answer = (row*col)
for x in range(row-7):
    for y in range(col-7):
        answer = min(answer, BFS(x, y, graph_original, black_board), BFS(x, y, graph_original, white_board))

print(answer)
