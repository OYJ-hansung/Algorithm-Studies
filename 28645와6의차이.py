import sys

graph = list(sys.stdin.readline().split())
def minimum(number):
    num_list = [i for i in number]
    for idx in range(len(number)):
        if num_list[idx] == '6':
            num_list[idx] = '5'
    return int(''.join(num_list))

def maximum(number):
    num_list = [i for i in number]
    for idx in range(len(number)):
        if num_list[idx] == '5':
            num_list[idx] = '6'
    return int(''.join(num_list))

min_array = []
max_array = []

for number in graph:
    min_num = minimum(number)
    max_num = maximum(number)

    min_array.append(min_num)
    max_array.append(max_num)

print(sum(min_array), sum(max_array))

