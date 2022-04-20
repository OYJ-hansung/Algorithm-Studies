import sys

N = int(sys.stdin.readline())
GWList = [sys.stdin.readline().strip() for _ in range(N)]
answer = 0

for word in GWList:
    Flag = True
    Group = []
    GLetter = 'R'
    for idx in range(len(word)):
        if word[idx] not in Group:
            GLetter = word[idx]
            Group.append(word[idx])
        elif (word[idx] in Group) and word[idx] != GLetter:
            Flag = False
            break
    if Flag ==True:
        answer +=1

print(answer)
         