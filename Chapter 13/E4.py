reader = open("test2.txt", "r")
linelist = []
while 1:
    tempstr = reader.readline()
    tempstr = tempstr[5:]
    linelist.append(tempstr)
    if len(tempstr) == 0:
        break
reader.close()

writer = open("test2.txt", "w")
for line in linelist:
    writer.write(line)
writer.close()
