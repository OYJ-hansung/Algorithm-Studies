import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
graph.sort()
left = 0
right = N-1
answer = 0

while left < right:
    left_num, right_num = graph[left], graph[right]
    summation = left_num + right_num
    if summation == x:
        answer +=1
        left +=1
        right -=1
    elif summation < x:
        left +=1
    else:
        right -=1
print(answer)
    
    
