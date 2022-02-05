import sys
row, col = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip())for _ in range(row)]
dx = [-1, 0, 1]
dy = [1, 1, 1]

def search(graph, start):
    global answer
    global flag
    for idx in range(3):
        x_cor = start[0] + dx[idx]
        y_cor = start[1] + dy[idx]
        if x_cor<0 or x_cor>row-1 or y_cor>col-1: #범위를 벗어났을때
            continue
        if graph[x_cor][y_cor] == 'x': # 건물 만났을떄
            continue
        elif y_cor>=col-1 and flag == False: # 끝에 도착했을떄
            answer +=1
            flag = True
            graph[x_cor][y_cor] = 'x'
            return True
        elif flag == False:
            graph[x_cor][y_cor] = 'x'
            search(graph, [x_cor, y_cor])
    return False

answer = 0
for idx in range(row):
    flag = False
    search(graph, [idx,0])

print(answer)

