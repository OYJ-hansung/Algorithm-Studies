import sys

def binary_search(array, target, start, end):
    global length
    if start>end:
        return False
    mid = (start + end)//2
    if array[mid] == target:
        length +=1
        return target
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

dut, bo = map(int, sys.stdin.readline().split())
graph_dut = [sys.stdin.readline().strip() for _ in range(dut)]
graph_bo = [sys.stdin.readline().strip() for _ in range(bo)]
graph_bo.sort()
length = 0

answer = list(filter(lambda x: binary_search(graph_bo, x, 0, bo-1) != False, graph_dut))
answer.sort()
print(length)
for idx in answer: 
    print(idx)




    