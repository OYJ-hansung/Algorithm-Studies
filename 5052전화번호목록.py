import sys

N = int(sys.stdin.readline())
graph = []
answer = []
for idx in range(N):
    K = int(sys.stdin.readline())
    graph.append([])
    for _ in range(K):
        graph[idx].append(sys.stdin.readline().strip())

for row in graph:
    row.sort()
    for idx in range(len(row)-1):
        if len(row[idx]) < len(row[idx+1]):
            if row[idx+1][:len(row[idx])] == row[idx]:
                answer.append('NO')
                break
    answer.append('YES')
    print(answer[0])
    answer.clear()            
            

