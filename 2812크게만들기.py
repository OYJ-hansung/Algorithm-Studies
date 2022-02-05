import sys
raw_length, eliminate_length = map(int,sys.stdin.readline().split())
index_list = [i for i in range(raw_length)]
raw_number = list(map(int,sys.stdin.readline().strip()))
raw_number_with_index = list(map(lambda x, y: [x, y], raw_number, index_list))
target_length = raw_length-eliminate_length
start = 0
answer = list()
idx = 0
print(raw_number_with_index)

while True:
    if len(answer) == target_length:
        for num in answer:
            print(num, end='')
        break

    if -(target_length-1)+idx<=-1:
        print(raw_number_with_index[start:-(target_length-1)+idx])
        max_tuple = max(raw_number_with_index[start:-(target_length-1)+idx])
        answer.append(max_tuple[0])
        start = max_tuple[1]+1
        print(max_tuple)
    else:
        print(raw_number_with_index[start:])
        max_tuple = max(raw_number_with_index[start:])
        answer.append(max_tuple[0])
        print(max_tuple)

    idx +=1
    # break
    

    
