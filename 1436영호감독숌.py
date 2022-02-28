import sys

N = int(sys.stdin.readline())
flag = False
original = '666'
version = 1
length = 1

while True:
    for idx in range(10**(length-1),int('6'*length)):
        new_title = str(idx)+original
        version +=1
        if version == N:
            print(int(new_title))
            flag = True
            break
    if flag == True:
        break

    new_title = original + ('0'*length)
    version +=1
    if version == N:
            print(int(new_title))
            flag = True
            break
    for idx in range(10**length):
        new_title = int(new_title)
        new_title +=1
        version +=1
        if version == N:
            print(int(new_title))
            flag = True
            break
    if flag == True:
        break
    
    for idx in range(int('6'*length)+1,10**length):
        new_title = str(idx)+original
        if version == N:
            print(int(new_title))
            flag = True
            break
        version +=1
        
    length +=1
    if flag == True:
        break