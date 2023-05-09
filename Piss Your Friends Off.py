#Expected Output: What an idiot you thought 1+1 was "number" 

import random

number = input("What is 1+1? ")
ran = random.randint(1,100)
answer = float(number) + float(ran)

if(answer != 2):
    print("Wow what an idiot! You thought 1+1 was", answer)
elif(answer == 2):
    print("Wow you're actually smart!")

#I hope all of your friends hate you after this. 