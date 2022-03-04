import sys
N = int(sys.stdin.readline())

if N <=9:
    print(N)
else:
    answer = 9
    for number in range(10, N+1):
        flag = True
        string_number = str(number)
        gap = int(string_number[1]) - int(string_number[0])
        for idx in range(2,len(string_number)):
            if (int(string_number[idx]) - int(string_number[idx-1])) !=gap:
                flag = False
                break
        if flag == True:
            answer += 1

    print(answer)