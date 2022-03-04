import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
combination = list(combinations(cards, 3))
max_num = 0

for a, b, c, in combination:
    summation = a+b+c
    if summation == M:
        max_num = summation
        break
    elif max_num<summation<=M:
        max_num = summation

print(max_num)