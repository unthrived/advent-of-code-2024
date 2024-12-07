path = 'data/day07.txt'
data = []
with open(path, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(': ')
        line[1] = list(map(int, line[1].split(' ')))
        data.append(line)
print(data)

def to_base_3(number):
    if number == 0:
        return "0"
    digits = []
    is_negative = number < 0
    number = abs(number)
    while number:
        digits.append(str(number % 3))
        number //= 3
    if is_negative:
        digits.append('-')
    return ''.join(reversed(digits))

def combination(result, row, a=True):
    if a:
        m = len(row)
        binary = 0
        for i in range(2**(m-1)):
            op = str(bin(binary))[2:]
            operations = [0] * (m-len(op)-1) # creates the op matrix, if 0 sum 1 mul
            for i in range(len(op)): operations.append(int(op[i]))
            m = len(row)
            total = row[0]
            for j in range(m-1):
                if operations[j]:
                    total = total + row[j+1]
                else:
                    total = total * row[j+1]
            print(operations, total, row, result)
            if result == total: return total
            binary += 1
        return 0
    else:
        m = len(row)
        binary = 0
        for i in range(3**(m-1)):
            op = str(to_base_3(binary))
            operations = [0] * (m-len(op)-1) # creates the op matrix, if 0 sum 1 mul 2 join
            for i in range(len(op)): operations.append(int(op[i]))
            m = len(row)
            total = row[0]
            for j in range(m-1):
                if operations[j] == 1:
                    total = total + row[j+1]
                if operations[j] == 2:
                    total = int(str(total) + str(row[j+1]))
                if operations[j] == 0:
                    total = total * row[j+1]
            print(operations, total, row, result)
            if result == total: 
                print(operations, total, row, result)
                return total
            binary += 1
        return 0
sum = 0
for i in range(len(data)):
    sum = sum+ combination(int(data[i][0]), data[i][1], a=False)
print(sum)