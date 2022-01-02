import sys
N, K = map(int, sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(N))
coins.sort(reverse = True)
answer = 0
for idx in coins:
    answer += K//idx
    K -= idx * (K//idx)
print(answer)

