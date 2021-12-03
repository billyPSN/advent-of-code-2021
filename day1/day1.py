from numpy import NaN
import pandas as pd

#part 1
df = pd.read_csv('./input.txt', header=None)
increases = 0
prevValue = NaN
for index, i in df.iterrows():
    if prevValue != NaN and prevValue < i[0]:
        increases += 1
    prevValue = i[0]

print(f"Total increases: {increases}")

#part 2
slider1 = []
slider2 = []
slider3 = []
increases = 0
prevValue = NaN

vals = []


for index, i in df.iterrows():
    #first population of sliders
    if not vals:
        if not slider1:
            slider1.append(i[0])
        elif len(slider1) == 1:
            slider1.append(i[0])
            slider2.append(i[0])
        elif len(slider1) == 2:
            slider1.append(i[0])
            slider2.append(i[0])
            slider3.append(i[0])
    #continual population of sliders
    else:
        slider1.append(i[0])
        slider2.append(i[0])
        slider3.append(i[0])

    #empty sliders
    if len(slider1) == 3:
        vals.append(sum(slider1))
        slider1.clear()
    elif len(slider2) == 3:
        vals.append(sum(slider2))
        slider2.clear()
    elif len(slider3) == 3:
        vals.append(sum(slider3))
        slider3.clear()
for i in vals:

    if prevValue != NaN and prevValue < i:
        increases += 1
    prevValue = i

print(f"Total 3 measurement slider increases: {increases}")


