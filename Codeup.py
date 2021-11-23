import sys

N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    queue.append(int(sys.stdin.readline()))
queue.sort()
for idx in range(N):
    print(queue[idx])