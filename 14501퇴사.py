import sys

N = int(sys.stdin.readline())
schedule = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

answer_list = [0]*(1000)
for idx in range(N-1, -1, -1):
    if schedule[idx][0] + idx > N:
        answer_list[idx] = answer_list[idx+1]
        continue
    else:
        answer_list[idx] = max(answer_list[idx+1], schedule[idx][1]+answer_list[idx+schedule[idx][0]])

print(answer_list[:N+1])
print(max(answer_list))