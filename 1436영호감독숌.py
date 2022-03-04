import sys
N = int(sys.stdin.readline())

title = 666
episode = 0

while True:
    if '666' in str(title):
        episode +=1
    if episode == N:
        print(title)
        break
    title +=1