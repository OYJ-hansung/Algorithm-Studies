import sys

N = int(sys.stdin.readline()) # 숫자의 길이
graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]for _ in range(101)]
graph[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for floor in range(1, N+1):
    for idx in range(10):
        if idx == 0:
            graph[floor][idx] = graph[floor-1][1]
        elif idx == 9:
            graph[floor][idx] = graph[floor-1][8]
        else:
            graph[floor][idx] = graph[floor-1][idx-1] + graph[floor-1][idx+1]

# print(graph)
total = sum(graph[N-1])
answer = total % 1000000000
print(answer)

