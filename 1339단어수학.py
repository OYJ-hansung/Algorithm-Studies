import sys

N = int(sys.stdin.readline())
alphabet = [0]*26
answer = 0
graph = list()
for idx in range(N):
    graph.append(str(sys.stdin.readline().strip()))

for idx in graph:
    i = 0
    while idx:
        now = idx[-1]
        alphabet[ord(now) - ord('A')] += pow(10, i)
        i+=1
        idx = idx[:-1]

alphabet.sort(reverse = True)
for i in range(9, 0, -1):
    answer += i * alphabet[9-i]

print(answer)