import sys

N = int(sys.stdin.readline())
nothing = []
graph = []
answer = 0
for _ in range(N):
    a = int(sys.stdin.readline())
    if a == 1:
        answer +=1
    if a <= 0:
        nothing.append(a)
    if a > 1:
        graph.append(a)
nothing.sort(reverse=True)
graph.sort()
for idx in range(len(graph)-1, -1, -2):
    if idx <=0:
        answer += graph[idx]
    else:
        answer += graph[idx]*graph[idx-1]

for idx in range(len(nothing)-1, -1, -2):
    if idx <=0:
        answer += nothing[idx]
    else:
        answer += nothing[idx]*nothing[idx-1]
print(answer)



