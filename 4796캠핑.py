import sys
graph = list()
i = 1
while True:
    a,b,c = list(map(int, sys.stdin.readline().split()))
    if a == 0 and b == 0 and c == 0:
        break
    graph.append([a, b, c])
for idx in graph:
    a, b, c = idx
    answer = a * (c//b)
    if c - (b * (c//b)) > a:
        answer += a
    else:
        answer += c - (b * (c//b))
    print('Case {0}:'.format(i), answer)
    i +=1


        