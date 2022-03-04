import sys
from itertools import permutations
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
calculator_temp = list(map(int, sys.stdin.readline().split()))
calculator = []

for idx in range(4):
    if idx ==0:
        for _ in range(calculator_temp[idx]):
            calculator.append('+')
    elif idx ==1:
        for _ in range(calculator_temp[idx]):
            calculator.append('-')
    elif idx ==2:
        for _ in range(calculator_temp[idx]):
            calculator.append('x')
    else:
        for _ in range(calculator_temp[idx]):
            calculator.append('/')

permutation = list(permutations(calculator, N-1))

min_answer = 10**10
max_answer = -10**10

for case in permutation:
    answer = numbers[0]
    for idx in range(1,N):
        if case[idx-1] == '+':
            answer = answer + numbers[idx]
        elif case[idx-1] == '-':
            answer = answer - numbers[idx]
        elif case[idx-1] == 'x':
            answer = answer * numbers[idx]
        else:
            if answer >0:
                answer = int(answer//numbers[idx])
            else:
                answer = -int((-answer )// numbers[idx])
    min_answer = min(min_answer, answer)
    max_answer = max(max_answer, answer)



print(max_answer)
print(min_answer)



