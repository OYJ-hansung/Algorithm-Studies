import sys
from collections import Counter

word = sys.stdin.readline().strip()
word_list = list(map(list,Counter(word).items()))
word_list.sort()
word_list_value = list(Counter(word).values())
even = 0
odd = 0

for num in word_list_value:
    if num%2==0: even +=1
    else: odd +=1

if len(word) %2 == 0: # 짝수
    answer_list = []
    if odd == 0:
        for letter in word_list:
            for _ in range(int(letter[1]/2)):
                answer_list.append(letter[0])
        answer_list = answer_list + list(reversed(answer_list))
        print(''.join(answer_list))
    else:
        print("I'm Sorry Hansoo")
else:
    answer_list = []
    if odd ==1:
        for letter in word_list:
            if letter[1]%2==0:
                for _ in range(int(letter[1]/2)):
                    answer_list.append(letter[0])
            else:
                odd_num = letter[0]
                if letter[1] > 1:
                    for _ in range(int((letter[1]-1)/2)):
                        answer_list.append(letter[0])

        answer_list_reversed = list(reversed(answer_list))
        answer_list.append(odd_num)

        answer_list = answer_list + answer_list_reversed
        print(''.join(answer_list))
    else:
        print("I'm Sorry Hansoo")