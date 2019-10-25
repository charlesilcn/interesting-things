from random import randint
money=1000 
while money >0:
    loop = False
    print ('you money%d'%money)
    debt=int(input('you debt is:' ))
    first=randint(1,6)+randint(1,6)
    print('your are %d' %first)
    if first == 7 or first==11:
        print('you win')
        money += debt
    if first==2 or first==3 or first==12:
        print('you lose')
        money -= debt
    else:
        loop = True
    while loop:
        loop = False
        current=randint(1,6)+randint(1,6)
        print('your are %d'%current)
        if current==7:
            print('you lose')
            money -= debt
        elif current==first:
            print('you win')
            money += debt
        else :
            loop = True
print('you are done!')



