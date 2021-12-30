import sys

def binary_search(array, target, start, end):
    if start>end:
        return 0
    mid = (start + end)//2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()
I = int(sys.stdin.readline())
answer = list(map(lambda x: binary_search(graph, int(x), 0, N-1), sys.stdin.readline().split()))

for idx in answer:
    print(idx, end = ' ')


    