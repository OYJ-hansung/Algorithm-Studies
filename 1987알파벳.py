import sys
sys.setrecursionlimit(10000)

def DFS(x, y, answer):
    global max_answer
    max_answer = max(max_answer, answer)
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if -1<nx<R and -1<ny<C:
            if visited[strings[nx][ny]] == 0:
                visited[strings[nx][ny]] = 1
                DFS(nx, ny, answer+1)
                visited[strings[nx][ny]] = 0


R, C = map(int, sys.stdin.readline().split())
strings = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]
visited = [0]*26
visited[strings[0][0]] = 1

max_answer = 1

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]

DFS(0, 0, 1)
print(max_answer)


