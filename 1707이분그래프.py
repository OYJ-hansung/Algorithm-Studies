import sys

sys.setrecursionlimit(10**7)
testcase = int(sys.stdin.readline())

def DFS(graph, start, color ,current_color):
    global flag

    flag = True
    color[start] = current_color

    for idx in graph[start]:
        if color[idx] == 9: # 방문하지 않았다면..
            new_color = not current_color
            flag = DFS(graph, idx, color, new_color)
            if flag == False:
                break
        else:               # 방문했었다면
            if color[idx] != current_color:
                continue
            else:
                return False
    return flag

answer = []

for _ in range(testcase):
    dot, line = map(int, sys.stdin.readline().split())
    color = [9]*(dot+1)
    graph = [[]for _ in range(dot+1)]

    for _ in range(line):
        dot1, dot2 = map(int, sys.stdin.readline().split())
        if dot1 not in graph[dot2]:
            graph[dot2].append(dot1)
        if dot2 not in graph[dot1]:
            graph[dot1].append(dot2)
            
    for idx in graph:
        idx.sort()

    flag = True
    for idx in range(1,dot+1):
        if color[idx] == 9:
            if not DFS(graph, idx, color, True):
                break 

    if flag:
        answer.append('YES')
    else:
        answer.append('NO')

for idx in range(testcase):
    print(answer[idx])