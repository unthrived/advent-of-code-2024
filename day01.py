import utils

path = 'data/day01.txt'
data = utils.read_txt(path)

tdata = list(map(list, zip(*data)))
tdata[0].sort()
tdata[1].sort()

length = 0
for i in range(len(data)):
    length = length + abs(tdata[1][i] - tdata[0][i])

print(length)

rep_col = []
sum = 0
for i in range(len(data)):
    counter = 0
    for j in range(len(data)):
        if data[i][0] == data[j][1]:
            counter += 1
    rep_col.append(counter)
for i in range(len(data)):
    sum = sum + data[i][0] * rep_col[i]

print(sum)