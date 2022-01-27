import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
for row in graph:
    row.sort()
    print(row[-3])