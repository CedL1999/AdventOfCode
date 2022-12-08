import string 
with open('input/input.txt') as f:
    formatted = [x.replace('\n','') for x in f.readlines() ]

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

tuppleList = []
#Create list a tupple with both halfs
for x in formatted:
    halfLenght =  int(len(x)/2)
    tuppleList.append((x[0: halfLenght], x[halfLenght : len(x)]))

#Iterate through each tupple to see the common letter from its two elements
sumOfCharacters = 0
for x in tuppleList:
    commonCharacter = ''.join(set(x[0]).intersection(x[1]))
    sumOfCharacters+=alphabet.index(commonCharacter) + 1 #adding 1 because the index count starts at 0

print(sumOfCharacters)
