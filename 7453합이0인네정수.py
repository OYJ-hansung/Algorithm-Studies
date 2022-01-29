import sys
from collections import Counter

def binarySearch(array, target, left, right):
    middle_idx = (left+right)//2
    print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        return True
    elif middle > target:
        binarySearch(array, target,left,middle_idx-1)
    elif middle < target:
        binarySearch(array, target,middle_idx+1,right)
    else: 
        return False


N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]
graph = list(map(list, zip(*graph)))
A, B, C, D = graph

AB_summation = []
for a in A:
    for b in B:
        AB_summation.append(a+b)

AB_Counter = Counter(AB_summation)
AB_Counter_list = list(AB_Counter.keys())
AB_Counter_list.sort()

answer = 0
for c in C:
    for d in D:
        Flag = binarySearch(AB_Counter_list, -(c+d), AB_Counter_list[0], AB_Counter_list[-1])
        if Flag == False:
            continue
        else:
            answer += AB_Counter[-(c+d)]

print(answer)