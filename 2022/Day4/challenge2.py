with open('input/input.txt') as f:
    formatted = [x.replace('\n','') for x in f.readlines() ]

tuppleList = []
#Create list a tupple with both halfs
for x in formatted:
    tuppleList.append((x.split(',')[0], x.split(',')[1]))

print(tuppleList)


overlapCount = 0
for x in tuppleList:

    elf1 = x[0]
    elf2 = x[1]

    #Creating list of each numbers in the given range
    elf1RangeList = list(range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1))
    elf2RangeList = list(range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1))

    #Just converting to string to be able to use intersection
    elf1String = ([str(x) for x in elf1RangeList])
    elf2String = ([str(x) for x in elf2RangeList])

    #All the characters common to the two list
    commonCharacter = (set(elf1String).intersection(elf2String))

    #If the lenght of the commonCharacter is the same as the lenght of one of the array, it means one has fully fit in
    if (len(commonCharacter)>=1):
        overlapCount+=1

print(overlapCount)