import sys

N = int(sys.stdin.readline())
seat = list(sys.stdin.readline().strip())
flag = False
answer = 0
idx = 0

while idx < N:
    if flag == False:
        if seat[idx] == 'L':
            flag = True
            idx+=2
            answer+=2
        else:
            idx +=1
            answer +=1
    else:
        if seat[idx] == 'L':
            idx+=2
            answer+=1
        else:
            idx +=1
            answer +=1
            

print(answer)
    
