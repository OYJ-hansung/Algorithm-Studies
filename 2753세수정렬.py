import sys

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

for num in numbers:
    print(num, end=' ')