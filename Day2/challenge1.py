
with open('input/input1.txt') as f:
    lines = f.readlines()

formatted = [x.replace('\n','') for x in lines ]

#Y, B is paper, 2
#X, A is rock, 1
#Z, C is scissors, 3
def calculatePoints(firstCol, secondCol):
    
    score = 0
    #Define point per secondCol
    #Papier
    if secondCol=='Y':
        score += 2
        #victoires, draws
        if firstCol=='B':
            score+=+3
        if firstCol =='A':
            score+=6

    #Roche
    elif secondCol=='X':
        score +=1
        #victoires, draws
        if firstCol=='A':
            score +=3
        if firstCol=='C':
            score+=6

    #Ciseau
    elif secondCol=='Z':
        score+= 3
        #victoires, draws
        if firstCol=='C':
            score+=3
        if firstCol=='B':
            score+=6
    return score

finalScore = 0
for x in formatted:
    finalScore+= calculatePoints(x[0], x[2])

print(f"The final score would be : {finalScore}")