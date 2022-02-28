import sys
from pprint import pprint
length = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(length)]

answer_list = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(graph, row, col):
    global answer

    if row<0 or row>=length or col<0 or col>=length:
        return False
    
    if graph[row][col] == 1:
        answer +=1
        graph[row][col] = 0
        # for idx in range(4):
        #     row = row + dx[idx]
        #     col = col + dy[idx]
        #     DFS(graph, row, col)
        DFS(graph, row, col+1)
        DFS(graph, row, col-1)
        DFS(graph, row+1, col)
        DFS(graph, row-1, col+1)
        return True
    return False



for row in range(length):
    for col in range(length):
        answer = 0
        if DFS(graph, row, col):
            answer_list.append(answer)
        

print(answer_list)
pprint(graph, width=100)

