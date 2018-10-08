reader = open("test.txt", "r")
linelist = []
while 1:
    tempstr = reader.readline()
    linelist.append(tempstr)
    if len(tempstr) == 0:
        break
reader.close()
linelist.reverse()

writer = open("test.txt", "w")
for line in linelist:
    writer.write(line)
writer.close()
