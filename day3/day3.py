from numpy import NaN
import pandas as pd

#part 1
df = pd.read_csv('./input.txt', header=None)
rowsList = []
for index, i in df.iterrows():
    vals = [int(n) for n in str(i[0])]
    rowsList.append(vals)
df_formatted = pd.DataFrame(rowsList)

gamma = []
epsilon = []
for column in df_formatted:
    mode = df_formatted[column].mode()
    gamma.append(str(int(mode[0])))
    if str(int(mode[0])) == '1':
        epsilon.append('0')
    else:
        epsilon.append('1')
gammaBin = (''.join(gamma))
epsilonBin = (''.join(epsilon))

part1 = int(gammaBin,2)* int(epsilonBin,2)
print(f'The answer to part 1 is {part1}')