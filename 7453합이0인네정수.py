import sys
from collections import defaultdict

N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]
graph = list(map(list, zip(*graph)))
A, B, C, D = graph


# A + B 배열과
# C + D 배열로 나누기 -> 시간 복잡도 줄이기 위해 (N^4 -> N^2)
first = defaultdict(int)
first = {}
for i in range(N):
    for j in range(N):
        A_B = A[i] + B[j]
        # first[A_B] += 1
        first[A_B] = first.get(A_B, 0) + 1


answer = 0
for i in range(N):
    for j in range(N):
        C_D = C[i] + D[j]
        # (A + B) + (C + D) == 0일 때 key값에 대한 value만큼 더해준다.
        # (C + D)의 -1을 곱한값이 first에 있으면 A + B + C + D가 0이다.
        if first.get(-C_D):
            answer += first.get(-C_D)

print(answer)