import sys
from itertools import combinations

hobits = [int(sys.stdin.readline())for _ in range(9)]
hobits.sort()
combination = list(combinations(hobits, 2))
All_hobits = sum(hobits)
flag = False

for hobitA, hobitB in combination:
    if (All_hobits - (hobitA+hobitB)) == 100:
        flag = True
        hobits.remove(hobitA)
        hobits.remove(hobitB)

        for idx in hobits:
                print(idx)
    if flag == True:
        break