from numpy import*

def readFile(text):
    f = open(text, 'r', encoding="UTF-8")
    inputData = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        inputData.append(line)
    return inputData

def getAnswer(inputData): #Находим число Каталана
    for i in inputData:
        i = i.split(" ")
        N = int(i[0])
        D = int(i[1])
        if (N%2)!=0:
            print("Введена нечетная длинна скобочного выражения")
        else:
            memo = []
            for i in range(N):
                memo.append([-1] * D)
            length, depth = N, D
            pairs = int(length / 2)
            print(depthLowerSum(pairs, depth, memo) - depthLowerSum(pairs, depth - 1, memo))
def depthLowerSum(pairs, depth, memo): #Находим количество выражений меньшей вложенности
    if memo[pairs - 1][depth - 1] != -1:
        return memo[pairs - 1][depth - 1]
    if pairs == 0 or depth == 1:
        memo[pairs - 1][depth - 1] = 1
        return 1
    s = 0
    for i in range(pairs):
        s += depthLowerSum(i, depth - 1, memo) * \
            depthLowerSum(pairs - 1 - i, depth, memo)
    memo[pairs - 1][depth - 1] = s
    return s

from os import listdir, getcwd

print(getcwd())
files = [i for i in listdir(getcwd()) if ".txt" in i]

for i, file in enumerate(files, start=1):
    try:
        print(f"Тест {i}")
        getAnswer(readFile(file))
    except Exception as e:
        print(e)


