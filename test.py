import sys

land, treasure = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(land+1)]

for idx in range(land-1):
    land1, land2, cost = map(int, sys.stdin.readline().split())
    graph[land1].append([land2, cost])
    graph[land2].append([land1, cost])

treasure_map = [0]*(land+1)
for idx in range(treasure):
    land, cost = map(int, sys.stdin.readline().split())
    treasure_map[land] = cost

answer_list=[]
def DFS(start, total_cost, total_treasure):
    visited = [False]*(land+1)
    visited[start] = True

    for arival, cost in graph[idx]:
        if not visited[arival]:
            visited[idx] = True
            total_cost += cost*2
            total_treasure = max(total_treasure, treasure_map[idx])
            DFS(idx, total_cost, total_treasure)

    answer_list.append([total_cost, total_treasure])


total_cost = 0
total_treasure = 0

DFS(1, 0, 0)

print(answer_list)