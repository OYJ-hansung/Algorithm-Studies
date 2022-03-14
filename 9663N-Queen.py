import sys

N = int(sys.stdin.readline())
answer = 0
location = [0]*N

def solution(row):
    global answer 

    if row == N:
        answer +=1
        return True

    for idx in range(N):
            location[row] = idx
            if check_if(row):
                solution(row+1)
    return False

def check_if(row):
    for before_row in range(row):
        if location[row]==location[before_row] or (abs(location[row] - location[before_row]) == abs(row-before_row)):
            print(location[row], row, '/', location[before_row], before_row)
            return False
    return True

solution(0)
print(answer)