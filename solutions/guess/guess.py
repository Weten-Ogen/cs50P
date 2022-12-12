import random

while True:
    lvl = int(input("enter a level : "))
    if (lvl > 0 ):
        num = int(random.randint(0, lvl))
        print(f"*************{num} ***********")
        print(f"I'm thinking of num between 1  and 100")
        n = int(input("guess the answer : "))
        if n < 0:
            n = int(input('guess the answer : ')) 
        elif n < num:
            print('too small ')
            n = int(input("guess the answer : "))
        elif n > num :
            print('too high ')
            n = int(input('guess the anwer '))
        else: 
            print('just right')
            break
            
    else: 
        lvl = int(input('enter a level: '))
        
        


    


       




