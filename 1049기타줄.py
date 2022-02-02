import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(M)]
graph = list(map(list, zip(*graph)))
set, individual = graph
set.sort()
individual.sort()
answer = 1000 * (N+1)

def min_cost(set, individual):
    cost_1 = individual*N
    if N<=6:
        cost_2 = set
        return min(cost_1, cost_2)
    else:
        cost_2 = (int(N//6)+1)*set
        cost_3 = (int(N//6))*set + (N - (int(N//6))*6)*individual
        print(cost_1,cost_2, cost_3)
        return min(cost_1, cost_2, cost_3)

answer = min_cost(set[0], individual[0])

print(answer)
