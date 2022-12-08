
with open('input/input1.txt') as f:
    lines = f.readlines()

formatted = [x.replace('\n','') for x in lines ]

#Y, B is paper, 2
#X, A is rock, 1
#Z, C is scissors, 3

#Si A et X : faut Z pour perdre
#Si A et Y : faut X pour draw
#Si A et Z : faut Y pour gagner

#Si B et X : faut X pour perder
#Si B et Y : faut Y pour draw
#Si B et Z : faut C

#Si C et X : faut Y
#Si C et Y : faut Z
#Si C et Z : faut X

def getNeeded(firstCol, secondCol):
    #A
    if firstCol == 'A':
        if secondCol=='X':
            return 'Z'

    if firstCol == 'A':
        if secondCol=='Y':
            return 'X'

    if firstCol == 'A':
        if secondCol=='Z':
            return 'Y'
    #B
    if firstCol == 'B':
        if secondCol=='X':
            return 'X'

    if firstCol == 'B':
        if secondCol=='Y':
            return 'Y'

    if firstCol == 'B':
        if secondCol=='Z':
            return 'Z'

    #C
    if firstCol == 'C':
        if secondCol=='X':
            return 'Y'

    if firstCol == 'C':
        if secondCol=='Y':
            return 'Z'

    if firstCol == 'C':
        if secondCol=='Z':
            return 'X'


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

    finalScore+= calculatePoints(x[0], getNeeded(x[0], x[2]))

print(f"The final score would be : {finalScore}")