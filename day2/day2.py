from numpy import NaN
import pandas as pd

#part 1
df = pd.read_csv('./input.txt', sep=' ', header=None)
depth = 0
horizontal = 0

for index, i in df.iterrows():
    if i[0] == 'forward':
        horizontal += i[1]
    elif i[0] == 'down':
        depth += i[1]
    elif i[0] == 'up':
        depth = depth - i[1]

part1 = depth*horizontal
print(f'The answer to part 1 is {part1}')

#part 2
depth = 0
horizontal = 0
aim = 0

for index, i in df.iterrows():
    if i[0] == 'forward':
        horizontal += i[1]
        depth += i[1]*aim
    elif i[0] == 'down':
        aim += i[1]
    elif i[0] == 'up':
        aim = aim - i[1]

part2 = depth*horizontal
print(f'The answer to part 2 is {part2}')
