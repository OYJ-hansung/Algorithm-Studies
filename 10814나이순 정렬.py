import sys

N = int(sys.stdin.readline())
answer = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

for idx in range(N):
    answer[idx].append(idx)

answer.sort(key = lambda x: int(x[0]))

for idx in answer:
    print(idx[0], idx[1])





