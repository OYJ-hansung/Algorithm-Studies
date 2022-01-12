import sys

N = int(sys.stdin.readline())
test_case = [int(sys.stdin.readline()) for _ in range(N)]
memorization = [9]*(max(test_case)+1)

def fiboncacci(idx):
    global answer_zero
    global answer_one
    if memorization[idx] !=9:
        answer_zero += memorization[idx][1]
        answer_one += memorization[idx][2]
        return memorization[idx][0]
    elif idx == 0 :
        answer_zero +=1
        return 0
    elif idx == 1 :
        answer_one +=1
        return 1
    else:
        return fiboncacci(idx-1) + fiboncacci(idx-2)

for idx in test_case:
    answer_zero = 0
    answer_one = 0
    memorization[idx] = [fiboncacci(idx), answer_zero, answer_one]
    print(answer_zero, answer_one)