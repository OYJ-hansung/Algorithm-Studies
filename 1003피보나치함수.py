import sys

N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline()) for _ in range(N)]

zero_lst = [1, 0, 1]
one_lst = [0, 1, 1]

def fibonacci(num):
    if num >= len(zero_lst):
        for idx in range(len(zero_lst), num+1):
            zero_lst.append(zero_lst[idx-1] + zero_lst[idx-2])
            one_lst.append(one_lst[idx-1] + one_lst[idx-2])
    print(zero_lst[num], one_lst[num])

for idx in graph:
    fibonacci(idx)



    