def dot_product(u, v):
    resul = 0
    for i in range(len(u)):
        resul += u[i] * v[i]
    return resul


print(dot_product([1, 2], [1, 4]))
