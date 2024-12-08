def check_line(row, data, b=False):
    for i in range(len(row)-1):
        for j in range(i+1, len(row)):
            check = [row[j], row[i]]
            if check in data:
                if not b:
                    return 0
                else:
                    row[j], row[i] = row[i], row[j]       
    if not b:
        return row[int((len(row))/2)]
    if b:
        return row

path = 'data/day05.txt'
data = []
test = []

with open(path, "r") as file:
    lines = file.readlines()
    comma = 0
    for line in lines:
        line = line.strip()
        if not line: 
            comma = 1
            continue
        if comma:
            test.append(list(map(int, line.split(','))))
        else:
            data.append(list(map(int, line.split('|'))))

sum = 0
for row in range(len(test)):
    sum = sum + check_line(test[row], data)
print(sum)
sum_b = 0
for row in range(len(test)):
    sum_b = sum_b + check_line(check_line(test[row], data, b=True), data)
    # first instance of checkline just sorts, second instance does A again
print(sum_b-sum)