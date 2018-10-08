def fibonacci_ite(term_num):
    num_list = [0, 1]
    if term_num <= 1:
        return num_list[term_num]
    else:
        for i in range(2, term_num + 1):
            num_list.append(num_list[i - 2] + num_list[i - 1])
        return num_list[term_num]


import time

t = time.clock()
print(fibonacci_ite(9000))
print(time.clock() - t)
