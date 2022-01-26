import sys

word = sys.stdin.readline().strip()
answer = list()
for idx in range(len(word)):
    answer.append(word[idx:])
answer.sort()
for word in answer:
    print(word)