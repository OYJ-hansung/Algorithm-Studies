import sys
sys.setrecursionlimit(10000)


def DFS(x, y, height):
    if x>=N or x<=-1 or y>=N or y<=-1:
        return False
    if graph[x][y] > height and visited[x][y] == False:
        visited[x][y] = True
        DFS(x, y+1, height)
        DFS(x, y-1, height)
        DFS(x+1, y, height)
        DFS(x-1, y, height)
        return True
    return False
            

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_height = max(map(max, graph))
min_height = min(map(min, graph))

max_answer = 1
for height in range(min_height, max_height+1):
    answer = 0
    visited = [[False]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if DFS(x, y, height) == True:
                visited[x][y] = True
                answer +=1
    max_answer = max(answer, max_answer)

print(max_answer)


