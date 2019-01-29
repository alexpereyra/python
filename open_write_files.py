with open("C:/Users/Alex/Documents/AWS/cloud formation template.txt") as input_file:
    for line in input_file:
        if len(line) < 4 : continue
        if line[0] == "D" and line[3] == 'c': print(line.strip())

###

description = []

with open("C:/Users/Alex/Documents/AWS/cloud formation template.txt") as input_file:
    for line in input_file:
        if len(line) < 4 : continue
        if line[0] == "D" and line[3] == 'c': description.append(line)

with open("C:/Users/Alex/Documents/AWS/ACG_fileW.txt", 'w') as output_file:
    for line in description:
        output_file.write(line)

description = []

with open("C:/Users/Alex/Documents/AWS/cloud formation template.txt") as input_file:
    for line in input_file:
        if len(line) < 4 : continue
        if line[0] == "O" and line[2] == 't': description.append(line)

###append

with open("C:/Users/Alex/Documents/AWS/ACG_fileW.txt", 'a') as output_file:
    for line in description:
        output_file.write(line)

###binary

with open ('guru-portfolio.zip', 'rb') as input_file:
    data = input_file.read()

type(data)
bytes

with open ('other.zip', 'wb') as output_file:
    output_file.write(data)
