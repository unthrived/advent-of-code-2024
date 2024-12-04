import utils
import re # if time ill do a solution w.o regex

# a
path = 'data/day03.txt'
data = utils.read_txt(path, numbers=False)
data = ''.join(data)
# print(data[0])

pattern = r'mul\(\d+,\d+\)'
pattern_do = r'do\(\)'
pattern_dont = r"don't\(\)"
matches = re.findall(pattern, data)
match_array = [m.start() for m in re.finditer(pattern, data)]
do_array = [m.start() for m in re.finditer(pattern_do, data)]
dont_array = [m.start() for m in re.finditer(pattern_dont, data)]

print(do_array)
print(dont_array)
print(match_array)
# print(matches)

sum = 0
for match in matches:
    content = match[4:-1]  
    x, y = map(int, content.split(','))
    # print(x, y)
    sum = sum + x * y 
print(sum)


# b brute forced the solution code, no time today :(
sum_b = 0
boolean = 1
boolean_do = []
boolean_match = []
for i in range(match_array[-1]+1):
    if i in do_array:
        boolean = 1
    if i in dont_array:
        boolean = 0
    boolean_do.append(boolean)
print(boolean_do)
print(len(matches))
for i in range(len(match_array)):
    boolean_match.append(boolean_do[match_array[i]])
print(boolean_match)

i=0
for match in matches:
    if boolean_match[i]:
        content = match[4:-1]  
        x, y = map(int, content.split(','))
        # print(x, y)
        sum_b = sum_b + x * y
    i = i+1
print(sum_b)
