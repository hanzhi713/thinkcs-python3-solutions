def add_vectors(u, v):
    sum = []
    for index in range(len(u)):
        sum.append(u[index] + v[index])
    return sum


print(add_vectors([1, 2], [1, 4]))
