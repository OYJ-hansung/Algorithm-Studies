import sys

N, K = map(int, sys.stdin.readline().split())
schedule = list(map(int, sys.stdin.readline().split()))
multitab = []
answer = 0

for idx in range(K): # 스케줄을 처음부터 끝까지 돈다.
    if schedule[idx] in multitab:
        continue
    elif len(multitab) < N:            # 멀티탭에 여유가 있다면
        multitab.append(schedule[idx])
    
    else:                                # 멀티탭에 여유가 없다면
            current_idx = -1
            target_idx = 0
            left_list = schedule[idx+1:]
            for multitab_device in multitab:
                if multitab_device in left_list: # 스케줄에서 다시 사용된다면..
                    if left_list.index(multitab_device) > current_idx:
                        current_idx = left_list.index(multitab_device)
                        target_idx = multitab.index(multitab_device)
                else:                            # 스케줄에서 다시 사용되지 않는다면..
                    target_idx = multitab.index(multitab_device)                    
                    break
            multitab[target_idx] = schedule[idx]
            answer +=1

print(answer)

