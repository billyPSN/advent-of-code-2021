import pandas as pd

def split_line(line: str):
    chars = 2
    list = []
    for i in range(round(len(line)/(chars+1))):
        startPos = i*(chars+1)
        list.append(int(line[startPos:startPos+chars]))
    return list


# Anything before the first line is the drawn numbers
def getDrawn(lineNum: int):
    drawnNumbers = []
    for position, line in enumerate(open(input_file)):
        if position < emptyLines[0]:
            # drawnNumbers.append(line.strip().split(','))
            drawnNumbers += line.strip().split(',')
    return drawnNumbers
   
# Every empty line after indicates the gap between 5x5 matrices
def getBoard(boardStart: int):
    matrix = []
    for position, line in enumerate(open(input_file)):
        if position > boardStart and position <= boardStart+5:
            matrix.append(split_line(line))
    # turn matrix into df for easy viewing
    df_matrix = pd.DataFrame(matrix)
    return df_matrix


def searchDf(df,val):
    for index, row in df.iterrows():
        for position,i in row.iteritems():
            if i == val:
                return index,position

def checkLines(df):
    #check columns
    for index, row in df.iterrows():
        if row.sum() == 5:
            return True
    for (index, col) in df.iteritems():
        if col.sum() == 5:
            return True

def getUnmatched(df_vals,df_check):
    sum = 0
    for index, row in df_check.iterrows():
        for position,i in row.iteritems():
            if i == 0:
                sum += df_vals.iloc[index,position]
    return sum

def bingo(boardStart: int):
    df_check = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    counter = 0
    dict_bingo = dict.fromkeys(bingoKeys)
    #get the board
    board = getBoard(boardStart)
    #loop through drawn numbers
    for i in drawnNumbers:
        counter += 1
        matched = searchDf(board,int(i))
        if matched:
            df_check.iloc[searchDf(board,int(i))] = 1
        if checkLines(df_check):
            dict_bingo['draws'] = counter
            dict_bingo['winningNum'] = i
            dict_bingo['unmatched'] = getUnmatched(board,df_check)
            break
    return dict_bingo


input_file = 'input.txt'
emptyLines = []
for position, line in enumerate(open(input_file)):
    if line == '\n':
        emptyLines.append(position)

bingoKeys = ['draws','winningNum','unmatched']
drawnNumbers = getDrawn(emptyLines[0])
winners = []


for i in emptyLines:
    print(f'about to get everything for line {i}')
    winners.append(bingo(i))
df_winners = pd.DataFrame(winners)
#get minimum draws position 
first_winner = df_winners['draws'].idxmin(axis=0)

winNum = df_winners.iloc[first_winner,1]
winUnma = df_winners.iloc[first_winner,2]
part1 = int(winNum)*int(winUnma)

print(part1)


firstLoser = df_winners['draws'].idxmax(axis=0)
loseNum = df_winners.iloc[firstLoser,1]
loseUnma = df_winners.iloc[firstLoser,2]
part2 = int(loseNum)*int(loseUnma)
print(part2)
