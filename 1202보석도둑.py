import sys
from heapq import heappush, heappop

N, K = map(int, sys.stdin.readline().split())

jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]
jewels.sort()
bags.sort()

answer = 0
answer_list = list()

for bag in bags:
    while jewels and bag>= jewels[0][0]:
        heappush(answer_list, -jewels[0][1])
        heappop(jewels)

    if answer_list:
        answer += heappop(answer_list)
    elif not jewels:
        break
print(-answer)



