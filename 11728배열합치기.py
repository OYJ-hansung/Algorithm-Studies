import sys

a, b = map(int, sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A.extend(B)
A.sort()
for idx in A:
    print(idx, end=' ')