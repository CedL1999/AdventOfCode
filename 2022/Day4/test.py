
listNum = list(range(1,4+1))
listNumString = ([str(x) for x in listNum])
listNum2 = list(range(2,3+1))
listNumString2 = ([str(x) for x in listNum2])

print(listNum)
print(listNum2)

commonCharacter = set(listNumString).intersection(listNumString2)
print(len(commonCharacter))
print(len(listNum2))
print(commonCharacter)