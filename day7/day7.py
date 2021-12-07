import pandas as pd

input = list(map(int, open('input.txt').read().strip().split(',')))
keys = ['pos','cost']
def getCost(list):
    costs = []
    for n in range(max(list)):
        #calculate the cost to get to n
        totalCost = 0
        for i in list:
            totalCost += abs(n-i)
        costDict = dict.fromkeys(keys)
        costDict['pos'] = n
        costDict['cost'] = totalCost
        costs.append(costDict)
    return costs

df = pd.DataFrame(getCost(input))
print(df)
print(df.min())

def getpart2Cost(list):
    costs = []
    for n in range(max(list)):
        #calculate the cost to get to n
        totalCost = 0
        for i in list:
            diff = abs(n-i)
            cost = (diff*(diff+1))/2
            totalCost += cost
        costDict = dict.fromkeys(keys)
        costDict['pos'] = n
        costDict['cost'] = totalCost
        costs.append(costDict)
    return costs


df = pd.DataFrame(getpart2Cost(input))
print(df)
print(df.min())
        
