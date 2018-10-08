def scalar_mult(s, v):
    resul = []
    for item in v:
        resul.append(item * s)
    return resul


print(scalar_mult(5, [1, 2]))
