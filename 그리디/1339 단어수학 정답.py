wordNum = input()
word = []
for i in range(int(wordNum)):
    temp = input()
    word.append(list(temp))
number = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
charDic = {}
for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] not in charDic:
            charDic[word[i][j]] = pow(10, len(word[i])-j-1)
        else:
            charDic[word[i][j]] += pow(10, len(word[i])-j-1)
keyList = list(charDic.items())
keyList.sort(key=lambda x : x[1],reverse=True)
print(keyList)
result=0
for i in keyList:
    result += number.pop(0)*charDic[i[0]]
print(result)
