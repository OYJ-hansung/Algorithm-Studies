import sys

T = int(sys.stdin.readline())
graph = [300, 60, 10]
answer = list()
for idx in graph:
    if T >= idx:
        answer.append(T//idx)
        T -= idx*(T//idx)
    else:
        answer.append(0)
if T ==0:
    for idx in answer:
        print(idx, end = ' ')
else:
    print(-1)
    
