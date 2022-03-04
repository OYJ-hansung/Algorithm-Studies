import sys
numbers = [True]*10001
numbers[2], numbers[4], numbers[6], numbers[8], numbers[10], numbers[12], numbers[14], numbers[16], numbers[18] = 0, 0, 0, 0, 0, 0, 0, 0, 0

for number in range(10, 10000+1):
    summation = number
    for idx in str(number):
        summation += int(idx)
        
    if summation < 10000:
        numbers[summation] = False

for idx in range(1,10000):
    if numbers[idx]:
        print(idx)
