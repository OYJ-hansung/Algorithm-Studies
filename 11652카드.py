import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
graph = [int(sys.stdin.readline())for _ in range(N)]
answer = -1

def how_many_nums(num):
    a = bisect_right(graph, num)
    b = bisect_left(graph, num)
    return (a-b)

for num in graph:
    temp = how_many_nums(num)
    if answer < temp:
        answer = temp
        real_answer = num

print(real_answer)