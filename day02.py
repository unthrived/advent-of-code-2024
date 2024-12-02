import utils

# a
path = 'data/day02.txt'
data = utils.read_txt(path)

# print(data)

count = 0
for i in range(len(data)):
    boolean = 1
    boolean_neg = 1
    remove = 1
    for j in range(len(data[i])-1):
        data[i][j] = data[i][j] - data[i][j+1]
    for j in range(len(data[i])-1):
        if not 0 < data[i][j] < 4: # maths
            boolean = 0
        if not -4 < data[i][j] <0:
            boolean_neg = 0
    count = count + boolean + boolean_neg

print(count)

# b
count = 0
for i in range(len(data)):
    boolean = 1
    boolean_neg = 1
    remove = 1
    remove_neg = 1
    for j in range(len(data[i])-1):
        data[i][j] = data[i][j] - data[i][j+1]
    for j in range(len(data[i])-1):
        if not 0 < data[i][j] < 4: # maths
            boolean = 0
            if remove:
                if 0 < data[i][j] + data[i][j+1] < 4: # weird maths
                    remove = 0
                    boolean = 1
                    j = j + 1
                else:
                    remove = 0
                    boolean = 1
            
        if not -4 < data[i][j] <0:
            boolean_neg = 0
            if remove_neg:
                if -4 < data[i][j] + data[i][j+1] < 0:
                    remove_neg = 0
                    boolean_neg = 1
                    j = j + 1
                else:
                    remove_neg = 0
                    boolean_neg = 1
    count = count + boolean + boolean_neg

print(count)
