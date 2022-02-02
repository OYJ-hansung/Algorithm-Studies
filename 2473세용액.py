import sys
n
N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()
print(graph)

fixed = 0
flag = False
answer = [graph[0], graph[1], graph[2]]

for idx in graph[:N-2]:
    fixed_num = graph[fixed]
    left = fixed +1
    right = N-1
    while left < right:
        summation = fixed_num + graph[left] +graph[right]
        if abs(summation) < abs(sum(answer)):
            answer = [fixed_num, graph[left], graph[right]]
        if summation <0:
            left +=1
        elif summation >0:
            right-=1
        else:
            flag = True
            break
    if flag == True:
        break
    fixed +=1

print(*answer)

