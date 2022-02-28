import sys
from pprint import pprint
sys.setrecursionlimit(10**7)

row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(row)]
answer = 0
dp = [[0 for _ in range(col)]for _ in range(row)]
print(dp)

def DFS(graph,x, y, higher_level):
    global answer
    if x<0 or y<0 or x>=row or y>=col:
        return False

    if x == (row-1) and y == (col-1) and graph[x][y]<higher_level:
        answer +=1
        return True

    
    if graph[x][y]<higher_level:
        lower_level = graph[x][y]
        DFS(graph, x, y+1, lower_level)
        DFS(graph, x+1, y, lower_level)
        DFS(graph, x, y-1, lower_level)
        DFS(graph, x-1, y, lower_level)
    return False

DFS(graph, 0, 0, 10001)
print(answer)