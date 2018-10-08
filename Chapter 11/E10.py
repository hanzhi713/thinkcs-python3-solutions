def replace(s, old, new):
    temp = s.split(old)
    temp2 = new.join(temp)
    return temp2


print(replace("Mississippi", "i", "I"))
