import sys

N = int(sys.stdin.readline())
answer = [int(sys.stdin.readline().strip()) for _ in range(N)]
answer.sort()

for idx in answer:
    print(idx)


