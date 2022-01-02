import sys
change = 1000 - int(sys.stdin.readline())
money = [500, 100, 50, 10, 5, 1]
count = 0
for idx in money:
    if change >= idx:
        count += change//idx
        change -= idx * (change//idx)
    if change == 0:
        break
print(count)