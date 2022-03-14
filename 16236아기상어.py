import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[]for _ in range(N)]

for idx_x in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph[idx_x] = row
    for idx_y in range(N):
        if row[idx_y] == 9:
            next_move = [idx_x, idx_y]

def BFS(x, y, size):
    global call_mom
    global next_move
    global time_addition

    visited = [[0 for _ in range(N)]for _ in range(N)]
    q = deque()
    q.append([x, y])

    found_minimum = 0
    minimum_list = []

    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] == 0 and size >= graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] +1
                    q.append([nx, ny])
                    if 0<graph[nx][ny]<size and found_minimum ==0: # 처음으로 최소거리를 찾았으면
                        found_minimum = visited[nx][ny]
                        minimum_list.append([nx, ny]) # 좌표값 저장하기
                    elif 0<graph[nx][ny]<size and visited[nx][ny] == found_minimum: # 이후로 최소거리를 또 찾았으면
                        minimum_list.append([nx, ny])
    #여기까지하면 minimum_list에 최소거리인 좌표값들이 모두 담겨 있을 것이다.
    if len(minimum_list) == 0:
        call_mom = True
    elif len(minimum_list) > 1:
        min_x = +N
        min_y = +N
        min_x_list = []
        for x, y in minimum_list:
            if min_x != min(min_x, x): # 가장 윗쪽 좌표가 업데이트 된다면
                min_x = min(min_x, x) #초기화 한 후에 새롭게 최소 좌표 추가
                min_x_list = []
                min_x_list.append([x, y])
            elif x == min_x:            # 가장 윗쪽에 있다면,.
                min_x_list.append([x, y])
            else:
                continue
        if len(min_x_list) ==1:     # 가장 윗쪽 좌표가 하나라면..
            next_move = min_x_list[0]
        else:                       # 가장 윗쪽 좌표가 여러개라면..
            for x, y in min_x_list:
                if min_y != min(min_y, y):
                    min_y = min(min_y, y)
                    next_move = [x, y]
    else:
        next_move = minimum_list[0] #거리가 최소인 좌표가 하나뿐일때 .. 

    time_addition = found_minimum

time = 0
call_mom = False
size = 2
cnt = 0
time_addition = 0

while True:
    previous_move = next_move
    graph[next_move[0]][next_move[1]] = 0
    BFS(next_move[0], next_move[1], size)
    time += time_addition
    if call_mom == True:
        print(time)
        break
    
    cnt +=1
    if cnt == size:
        size +=1
        cnt = 0