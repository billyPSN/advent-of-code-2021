import re
from collections import Counter

input = open('input.txt').read()
lines = []

for n in input.strip().splitlines():
    line = []
    for i in re.split(r'\W+', n):
        line.append(int(i))
    lines.append(line)
# print(lines)

# make sure that it's a flat line
def validLine(x1,y1,x2,y2):
    return x1 == x2 or y1 == y2

# calculate the points that are covered off with each coordinate
def line(x1, y1, x2, y2):
    points = []
    lx, ly = abs(x2 - x1), abs(y2 - y1)
    l = max(lx, ly)
    for i in range(l + 1):
        x = x1 + round((x2 - x1) / l * i)
        y = y1 + round((y2 - y1) / l * i)
        points.append((x, y))
    return points

#count each time that the points occur only for flat lines
#part 1
part1 = Counter()
for l in filter(lambda l: validLine(*l), lines):
    part1.update(line(*l))

print(len([i for i in part1.items() if i[1] > 1]))

#just remove the filter and you're set
#part 2
part2 = Counter()
for l in lines:
    part2.update(line(*l))
print(len([i for i in part2.items() if i[1] > 1]))