import sys

N = int(sys.stdin.readline())

# graph = [['0'] for _ in range(91)]
# graph[0] = ['0','1']
# graph[1] = ['0', '10']

# for floor in range(2,N):
#     for idx in range(1,len(graph[floor-1])):
#         if graph[floor-1][idx][-1] == '1':
#             a = graph[floor-1][idx] + '0'
#             graph[floor].append(a)
#         else:
#             a, b = graph[floor-1][idx] + '0', graph[floor-1][idx] + '1'
#             graph[floor].extend([a, b])

# answer = len(graph[N-1])-1
# print(answer)

graph = [0]*100
graph[0] = 1
graph[1] = 1 

for idx in range(2, N):
    graph[idx] = graph[idx-1] + graph[idx-2]

print(graph[N-1])