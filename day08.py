import utils

# a
path = 'data/day08.txt'
data = utils.read_txt(path, numbers=False)
# print(ord('a'),ord('z'), ord('Z'), ord('0'), ord('9'), ord('.'))
n = len(data)
m = len(data[0])
antinodes = [[0 for _ in range(3*n)] for _ in range(3*m)] # padding
def get_indices(x, y, a = True, left = True): 
    """
    given x, y two points in a plane returns two points that are equidistant
    7 1 , 2 0 -> -3 -1 , 12 2
    when a is False, returns the left/right equidistant point
    """
    if a:
        first = [None]*2
        first[0] = 2*x[0]-y[0]
        first[1] = 2*x[1]-y[1]
        second = [None]*2
        second[0] = 2*y[0]-x[0]
        second[1] = 2*y[1]-x[1]
        return first, second
    else:
        if left:
            first = [None]*2
            first[0] = 2*x[0]-y[0]
            first[1] = 2*x[1]-y[1]
            return first, x
        else:
            second = [None]*2
            second[0] = 2*y[0]-x[0]
            second[1] = 2*y[1]-x[1]
            return y, second


for ascii in range(48, 123):
    found = []
    character = chr(ascii)
    for i in range(n):
        for j in range(m):
            if data[i][j] == character: 
                found.append([i, j])
    #print(character, found)
    for i in range(len(found)-1):
        for j in range(i+1, len(found)):
            #print(found[i], found[j])
            #print(get_indices(found[i], found[j]))
            x, y = get_indices(found[i], found[j])
            antinodes[x[0]+n][x[1]+m] = 1
            antinodes[y[0]+n][y[1]+m] = 1
sum = 0
for i in range(n, 2*n):
    for j in range(n, 2*n):
        sum = sum + antinodes[i][j]
print(sum)

# B

for ascii in range(48, 123):
    found = []
    character = chr(ascii)
    for i in range(n):
        for j in range(m):
            if data[i][j] == character: 
                found.append([i, j])
    #print(character, found)
    for i in range(len(found)-1):
        for j in range(i+1, len(found)):
            #print(found[i], found[j])
            #print(get_indices(found[i], found[j]))
            x, y = get_indices(found[i], found[j], a=False, left=True)
            antinodes[x[0]+n][x[1]+m] = 1
            antinodes[y[0]+n][y[1]+m] = 1
            while n>x[0]>=0 and n>x[1]>=0 and n>y[1] >=0 and n>y[0]>=0:
                antinodes[x[0]+n][x[1]+m] = 1
                antinodes[y[0]+n][y[1]+m] = 1
                x, y = get_indices(x, y, a=False, left=True)
            x, y = get_indices(found[i], found[j], a=False, left=False)
            antinodes[x[0]+n][x[1]+m] = 1
            antinodes[y[0]+n][y[1]+m] = 1
            while m>x[0]>=0 and m>x[1]>=0 and m>y[1] >=0 and m>y[0]>=0:
                antinodes[x[0]+n][x[1]+m] = 1
                antinodes[y[0]+n][y[1]+m] = 1
                x, y = get_indices(x, y, a=False, left=False)
sum = 0
for i in range(n, 2*n):
    for j in range(n, 2*n):
        sum = sum + antinodes[i][j]
print(sum) #1218