import sys

parking_space = int(sys.stdin.readline())
number_of_planes = int(sys.stdin.readline())
graph = [int(sys.stdin.readline()) for _ in range(number_of_planes)]
graph_set = set(graph)
print(min(len(graph_set), number_of_planes))