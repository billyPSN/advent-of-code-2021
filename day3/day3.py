from numpy import NaN
import pandas as pd

def read_file(file_str: str):
    df = pd.read_csv(file_str, header=None,dtype='str')
    rowsList = []
    for index, i in df.iterrows():
        vals = [str(n) for n in str(i[0])]
        rowsList.append(vals)
    return pd.DataFrame(rowsList)

#part 1
def get_part1(df: pd.DataFrame):
    gamma = []
    epsilon = []
    for column in df:
        mode = df[column].mode()
        gamma.append(str(int(mode[0])))
        if str(int(mode[0])) == '1':
            epsilon.append('0')
        else:
            epsilon.append('1')
    gammaBin = (''.join(gamma))
    epsilonBin = (''.join(epsilon))
    return str(gammaBin),str(epsilonBin)

def get_decimal(val: str):
    return int(val,2)
    #return int(gamma,2)*int(epsilon,2)

#part 2

def get_part2(df: pd.DataFrame, value: str):
    count = 0
    for column in df:
        one = len(df.loc[df[column] == '1'])
        zero = len(df.loc[df[column] == '0'])
        if value == 'oxygen':
            if one >= zero:
                newNum = '1'
            else:
                newNum = '0'
        elif value == 'scrubber':
            if one >= zero:
                newNum = '0'
            else:
                newNum = '1'
        df = df.loc[df[column] == newNum]
        df.reset_index(drop=True,inplace=True)
        count = len(df.index)
        if count == 1:
            return ''.join(df.loc[0,:].values.flatten().tolist())

df = read_file('./input.txt')

gamma,epsilon = get_part1(df)
print(f'The answer to part 1 is {get_decimal(gamma)*get_decimal(epsilon)}')

oxy = get_part2(df,'oxygen')
co2 = get_part2(df,'scrubber')
print(f'The answer to part 2 is {get_decimal(oxy)*get_decimal(co2)}')


