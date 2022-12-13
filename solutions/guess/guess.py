import random
def guess_game():
    while True:
        # Get the level
        l = int(input('Level :  '))
        if l > 0:
            # Pick a number btwn (1,100)
            n =random.randint(1,l + 1)
        else:       
            # Reprompt the user
            l = int(input('level :  '))

        while True:
            # Prompt the user 
            ans = int(input('Guess : '))
            # If the l is greater than 1
            if ans < n :
                print('Just Small!')
                ans = int(input('Guess : '))
            elif ans == n :
                print('Just Right!')
                break
            else:
                print('Too large!')
                ans = int(input('Guess : '))
        return
    
            
    
        
        
if __name__ == "__main__":
    guess_game()      

            
        

        
        


    


       




