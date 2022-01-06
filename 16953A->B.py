import sys

A, B = map(str,sys.stdin.readline().split())
count = 1
while B != A:
    if int(B)%2==0:
        B = str(int(int(B)/2))
        count +=1
    elif B[-1] == '1':
        B = B[:-1]
        count +=1
    else:
        count = -1
        break
    if int(B) < int(A):
        count = -1
        break
    
print(count)


