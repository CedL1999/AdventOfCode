import string 
with open('input/input.txt') as f:
    formatted = [x.replace('\n','') for x in f.readlines() ]

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

tuppleList = []
#Create list a tupple with each three thirds
for x in range (0, len(formatted), 3):
    tuppleList.append((formatted[x], formatted[x+1], formatted[x+2]))

#Iterate through each tupple to see the common letter from its three elements
sumOfCharacters = 0
for x in tuppleList:
    commonCharacter = ''.join(set(x[0]).intersection(x[1]).intersection(x[2]))
    sumOfCharacters+=alphabet.index(commonCharacter) + 1 #adding 1 because the index count starts at 0

print(sumOfCharacters)
