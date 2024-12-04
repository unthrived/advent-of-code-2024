import utils
# from math import sin, cos, pi

data = utils.read_txt('data/day04.txt', numbers=False)
n = len(data)
m = len(data[0])-1

padded_data = [['O'] * (m + 6) for _ in range(n + 6)] # solely for list out of range :)

for i in range(n):
    for j in range(m):
        padded_data[i + 3][j + 3] = data[i][j]

angle = { # i wanted to do it with fancy sin and cos, im not proud (maybe) of this dict
    0: [1, 0],
    45: [1, 1],
    90: [0, 1],
    135: [-1, 1],
    180: [-1, 0],
    225: [-1, -1],
    270: [0, -1],
    315: [1, -1]
}

# a
count = 0

for i in range(3, n+6): # more loops
    for j in range(3, m+6):
        if padded_data[i][j] == 'X':
            for alpha in range(8):
                angle_x, angle_y = angle[45*alpha][0], angle[45*alpha][1]
                if padded_data[i+angle_x][j+angle_y] == 'M':
                    if padded_data[i+2*angle_x][j+2*angle_y] == 'A':
                        if padded_data[i+3*angle_x][j+3*angle_y] == 'S':
                            count += 1
print(count)

# b essentially searching for A's and whether if it has two Ms and two As
count = 0

for i in range(3, n+6):
    for j in range(3, m+6):
        if padded_data[i][j] == 'A':
            count_M = 0
            count_S = 0
            for alpha in range(4):
                angle_x, angle_y = angle[90*alpha+45][0], angle[90*alpha+45][1]
                if padded_data[i+angle_x][j+angle_y] == 'M':
                    print('M')
                    count_M += 1
                if padded_data[i+angle_x][j+angle_y] == 'S':
                    print('S')
                    count_S += 1
            print(count_M, count_S)
            if count_M == 2 and count_S == 2: # we have a X shaped MAS
                if padded_data[i+1][j+1] != padded_data[i-1][j-1]: 
                    # Just check if opposites are different -> Correct X shape
                    count += 1
print(count)

                