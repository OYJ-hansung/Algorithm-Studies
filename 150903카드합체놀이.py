import sys

n,m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    card.sort()
    summation = sum(card[:2])
    card[0] = summation
    card[1] = summation


print(sum(card))
