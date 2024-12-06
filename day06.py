import utils

data = utils.read_txt('data/day06.txt', numbers=False)
data = [list(row) for row in data]
n = len(data)
m = len(data[0])
# print(data, n, m)

moves = {
    0: [0, -1], # left
    1: [-1, 0], #  up
    2: [0, 1], # right 
    3: [1, 0] # down
}

# find start
for i in range(n): 
    for j in range(m): 
        if data[i][j] in ['^', '>', '<', 'v']:
            current_x, current_y = i, j
            if data[i][j] == '^':
                direction = 1
            if data[i][j] == '>':
                direction = 2
            if data[i][j] == 'v':
                direction = 3
            if data[i][j] == '<':
                direction = 0
            data[i][j] = 1

# print(direction, current_x, current_y)

def a(data, current_x, current_y, direction):
    n = len(data)
    m = len(data[0])
    loop = 0
    while (0<=current_x+moves[direction][0]<n and 0<=current_y+moves[direction][1]<m):
        if data[current_x+moves[direction][0]][current_y+moves[direction][1]] != '#':
            current_x = current_x+moves[direction][0]
            current_y = current_y+moves[direction][1]
            data[current_x][current_y] = 'X'
            #print(current_x, current_y, direction)
        else:
            direction = (direction + 1) % 4
        loop += 1
        # print(current_x, current_y, loop)
        if loop > 2*n*m: return 0
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'X': 
                count += 1
                # print('hi', count)
            # lazy (but fast) way of checking there's a loop.
    return(count)
print('a', a(data, current_x, current_y, direction))

count_b = 0
for i in range(n):
    for j in range(m):
        if not (i == current_x and j == current_y):
            obstacle = [row[:] for row in data] 
            # SPENT 1 HOUR HERE BECAUSE obstacle = data.copy() modifies data
            obstacle[i][j] = '#'
            loop = a(obstacle, current_x, current_y, direction)
            if loop == 0:
                count_b += 1
print(count_b)
