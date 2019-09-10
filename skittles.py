#This program is written to generate a random amount of skittles and asks the user to guess the right amount
#The program will tell the value of the user's guess in comparison to the number generated
#This program is written by Ann
import random

skittles = random.randint(0,1023) 

while True:
    guess = int(input("Enter a guess: "))
    if guess == skittles:
        print("You got it!")
        break
    if guess < skittles:
        print("Too low! Guess again.")
    elif guess > skittles:
        print("Too high! Guess again.")

print("That's the right amount of skittles!")

#This is an alternative way for this program as discussed with Mrs. Richardson earlier
#Written by Ann with the help of Mrs. Richardson 
''' 
guess = int(input("Enter a guess: "))

while guess != skittles:
    if guess > skittles:
      print("Too big. Guess again.")
    elif guess < skittles:
      print("Too small. Guess again.")
    guess = int(input("Enter a guess: "))
    
print("Good job, you got it!")
'''
