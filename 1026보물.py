import sys

N =  int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)
answer = 0
for idx in range(N):
    answer += A[idx]*B[idx]
print(answer)


