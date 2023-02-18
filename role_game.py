from random import randint
j1=50
j2=50
while j1>0 :
    degatj1=randint(5,10)
    degatj2=randint(5,15)
    potion=randint(15,50)
    cj2=randint(1,2)
    l=input('prendre potion (2) ou combatre (1) : ')
    if int(l) == 1 and int(cj2)==1:
        j1=j1-degatj2
        j2=j2-degatj1
        print(f'votre santer est {j1} la puissance de votre attacke est {degatj1} le degat est de {degatj2}')
        print(f'la santer de l"enemi est  {j2} la puissance de votre attacke est {degatj2} le degat est de {degatj1}')
        continue
    elif int(l)==2 and int(cj2)==1:
        j1=j1-degatj2+potion
        print(f'votre santer est {j1} le pouvoir de la potion est {potion}  le degat est de {degatj2}')
        print(f'la santer de l"enemi est  {j2}')
        continue
    elif int(l)==1 and int(cj2)==2:
        j2=j2-degatj1+potion
        print(f'votre santer est {j1}')
        print(f'la santer de l"enemi est  {j2} le pouvoir de la potion est {potion}  le degat est de {degatj1} ')
        continue
    elif int(l)==2 and int(cj2)==2:
        j1=j1+potion
        j2=j2+potion
        print(f'votre santer est {j1}')
        print(f'la santer de l"enemi est  {j2}')
        continue
    elif j1>0 and j2==0:
        print('gagner')
        break
print('loser')    