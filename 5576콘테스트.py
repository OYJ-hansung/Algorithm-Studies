import sys

graph = [int(sys.stdin.readline())for _ in range(20)]
A = sorted(graph[:10], reverse=True)
B = sorted(graph[10:], reverse=True)
print(sum(A[:3]), end=' ')
print(sum(B[:3]))