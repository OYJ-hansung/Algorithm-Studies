import sys
from bisect import bisect_left, bisect_right


def count(list, num):
    a = bisect_left(list, num)
    b = bisect_right(list, num)
    return b-a

N = int(sys.stdin.readline())
for _ in range(N):
    K = int(sys.stdin.readline())
    list_1 = list(map(int, sys.stdin.readline().split()))
    list_1.sort()
    L = int(sys.stdin.readline())
    list_2 = list(map(int, sys.stdin.readline().split()))
    
    for num in list_2:
        print(count(list_1, num))
