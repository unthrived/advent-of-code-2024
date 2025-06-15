import utils

# a
path = 'data/day09.txt'
data = utils.read_txt(path, numbers=False)
test = '12345'
test = '2333133121414131402'
blocks = []
result = []
# print(data[0])
test = data[0]
count = 0
for i in range(0, len(test)): 
    if (i+1)%2:
        for j in range(int(test[i])):
            blocks.append(count)
        count = count + 1
    else:
        for j in range(int(test[i])):
            blocks.append('.')
    # count = count + 1

for i in range(len(blocks)):
    if blocks[i] != '.':
        # print('i', i)
        result.append(blocks[i])

j = len(result)-1
changes = 0
for i in range(len(blocks)):
    if blocks[i] == '.':
        blocks[i] = result[j]
        j = j-1
        changes += 1

blocks = blocks[0:len(blocks)-changes]


print(blocks, len(blocks))
print(result, len(result))

total = 0
for i in range(len(blocks)):
    total = total + blocks[i] * i

print(total)