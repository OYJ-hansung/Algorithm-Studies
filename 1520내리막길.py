import sys
sys.setrecursionlimit(10**7)

row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(row)]
answer = 0
dp = [[-1 for _ in range(col)]for _ in range(row)]

def DFS(graph,x, y, higher_level):
    global answer

    if x == (row-1) and y == (col-1) and graph[x][y]<higher_level: # target arrived
        dp[x][y] = 1
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    answer = 0
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nx = x + dx
        ny = y + dy
        if 0<=nx<row and 0<=ny<col:
            if graph[nx][ny]<graph[x][y]: # if its lower
                answer += DFS(graph, nx, ny, graph[x][y]) # recursive

    dp[x][y] = answer
    return dp[x][y]

print(DFS(graph, 0, 0, 10001))