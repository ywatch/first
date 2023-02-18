from random import randint
numero=randint(0,100)
essai=5
i=0
print("***le jeux commence***")
while essai>0:
    l=input('taper un numero : ') 
    i=i+1
    if numero>int(l):
        print(f"{i} : le nombre est plus grand que {l}") 
        essai=essai-1
        continue
    elif numero<int(l):    
        print(f"{i} : le nombre est plus petit que {l}") 
        essai=essai-1
        continue
    elif numero==int(l):
        print('le numero est bon ')
        break
    else:
        print('erreur')    
        break
if essai==0:
    print('loser')