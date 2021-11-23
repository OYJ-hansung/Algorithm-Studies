#리스트를 이용한 풀이
def solution(participant, completion):
    for com in completion:
        if com in participant:
            if len(participant) ==1:
                return participant[0]
            participant.remove(com)
    return participant[0]


#counter를 이용한 풀이
from collections import Counter

def solution(participant, completion):
    cnt = Counter()
    for p in participant:
        cnt[p] += 1
    for c in completion:
        cnt[c] -= 1
    return list(x for x,y in cnt.items() if y == 1).pop();