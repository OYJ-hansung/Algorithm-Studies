import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()
left = 0
right = N-1
value = 10**10

while left < right:
    left_num, right_num = graph[left], graph[right]
    summation = left_num + right_num

    if abs(summation) < value:
        value = abs(summation)
        answer = [left_num, right_num]
    
    if summation > 0:
        right -=1
    elif summation < 0:
        left +=1
    else:
        answer = [left_num, right_num]
        break


for idx in answer:
    print(idx, end=' ')