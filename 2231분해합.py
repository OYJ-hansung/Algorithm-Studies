import sys

N = int(sys.stdin.readline())
flag = False
for number in range(1,N+1):
    provider = number
    for idx in str(provider):
        provider += int(idx)
    if provider == N:
        print(number)
        flag = True
        break

if flag == False:
    print(0)