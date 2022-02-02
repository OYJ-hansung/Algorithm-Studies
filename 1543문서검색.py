import sys

doc = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()



target_length = len(target)
doc_length = len(doc)
idx = 0
answer = 0

while idx <=(doc_length-target_length+2):
    if doc[idx:idx+target_length] == target:
        idx += target_length
        answer +=1
    else:
        idx +=1

print(answer)
