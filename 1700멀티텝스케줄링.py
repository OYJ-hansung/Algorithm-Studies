import sys
from bisect import bisect_left

def intersect(a, b):
    return list(set(a) & set(b))
def subtract(a, b):
    return list(set(a) - set(b))

multi_tab_num, K = map(int, sys.stdin.readline().split())
device_order = list(map(int, sys.stdin.readline().split()))
multi_tab = []
answer = 0

for idx in range(K):
    if device_order[idx] not in multi_tab and len(multi_tab) <multi_tab_num: # 전자기기가 꽂혀있지 않으며, 아직 다 차 있지 않았을떄
        multi_tab.append(device_order[idx])
    elif device_order[idx] not in multi_tab and len(multi_tab) == multi_tab_num: # 전자기기가 꽂혀있지 않으며, 다 차 있을떄
        answer +=1
        if idx == K-1:
            break
        elif len(device_order[idx+1:]) < multi_tab_num:
            list_behind = device_order[idx+1:]
        else:
            list_behind = device_order[idx+1:idx+1+multi_tab_num]

        intersect_multitab = intersect(list_behind,multi_tab)
        if len(intersect_multitab) == multi_tab_num: #3개가 다 있어
            target_index = bisect_left(multi_tab, list_behind[0])
            print(target_index)
            del multi_tab[target_index]
            multi_tab.append(device_order[idx])
        else:
            subtract_multitab = subtract(multi_tab, list_behind)
            target_index = bisect_left(multi_tab, subtract_multitab[0])
            del multi_tab[target_index]
            multi_tab.append(device_order[idx])

print(answer)