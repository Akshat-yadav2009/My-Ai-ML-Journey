"""Number guessing game"""

import random
secret=random.randint(1,100)
attempts=int(input("how many attempte you want to play" ))
i=0
while i<attempts:
    guess=int(input("enter your number:- ")) 
    print("you guessed ",guess) 

    if secret==guess:
        print("you guessed correctly")  
        break
    elif secret>guess:
        print("you guessed high") 
    else:
        print("you gussed low")

    i+=1

print("the number was",secret)