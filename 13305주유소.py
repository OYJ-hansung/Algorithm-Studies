import sys

N = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
min_cost = cost[0]
len_sum = length[0]

idx = 1
answer = -1

while idx <=N-2:
    if cost[idx] <= min_cost:
        answer +=min_cost*len_sum
        len_sum = 0
        idx +=1
        if idx == N-2:
            len_sum = length[-1]
            answer +=min_cost*len_sum
        min_cost = cost[idx]
    else:
        len_sum += length[idx-1]
        idx +=1

print(answer)