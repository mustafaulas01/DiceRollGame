import random

diceComputer=[1,2,3,4,5,6]
diceMe=[1,2,3,4,5,6]

win=0
lose=0
draw=0
counter=0


while counter<3:
    random.shuffle(diceComputer)
    random.shuffle(diceMe)
    me=random.choice(diceMe)
    computer=random.choice(diceComputer)
    print('Computer Dice :' + str(computer)+' Benim Zar: '+str(me))
    if computer>me:
        print('You Lose the Game')
        lose=lose+1
    elif computer<me:
        print('You Win The Game')
        win=win+1
    else:
        print('Draw')
        draw=draw+1


    sayac=sayac+1
print('***********************************************************')
print('Win :' + str(win) +'Lose :'+ str(lose)+' Draw:'+ str(draw))