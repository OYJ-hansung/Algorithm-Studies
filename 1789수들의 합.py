import sys

N = int(sys.stdin.readline())
T = 1
increase = 2
answer = 0
while True:
    if (T+ increase > N):
        break
    T += increase
    increase +=1
    answer +=1
    
answer +=1
print(answer)


