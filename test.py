num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    answer = []
    for idx in num_list:
            if idx%2!=0:
                answer.append(idx)
    return answer
    
print(get_odd_num(num_list))