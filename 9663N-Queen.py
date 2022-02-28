import sys

N = int(sys.stdin.readline())
answer = 0
location = [0]*N

def check(row):
    for idx in range(row):
        if (location[row] == location[idx]) or (abs(row-idx) == abs(location[row]-location[idx])):
            return False
    return True

def solution(row):
    global answer

    if row == N:
        answer +=1
        return 0
    
    for column in range(N):
        location[row] = column # (row, column)
        if check(row):
            solution(row+1)

solution(0)
print(answer)