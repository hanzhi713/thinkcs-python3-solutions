def cross_product(u, v):
    resul = []
    resul.append(u[1] * v[2] - u[2] * v[1])
    resul.append(u[2] * v[0] - u[0] * v[2])
    resul.append(u[0] * v[1] - u[1] * v[0])
    return resul


print(cross_product([1, 3, 6], [2, 4, 9]))
