
days = 256
ages = []
fish = [0,0,0,0,0,0,0,0,0]

with open('input.txt') as f:
    ages = f.readline().split(',')
    ages = [int(i) for i in ages]

for lantern in ages:
    fish[lantern] +=1

for i in range(days):
    zero_val = fish[0]
    for i in range(len(fish)-1):
        fish[i] = fish[i+1]
    fish[6] = fish[6] + zero_val
    fish[8] = zero_val

print(f'total number of fish after {days} days is {sum(fish)}')