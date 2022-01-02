import sys

N = list(map(int, sys.stdin.readline().strip()))
if 0 in N and sum(N)%3 == 0:
    N.sort(reverse=True)
    for idx in N:
        print(idx, end = '')
else:
    print(-1)


    