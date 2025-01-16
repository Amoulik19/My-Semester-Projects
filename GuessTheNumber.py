#Aarav Moulik
#Period 1
#11/11/24
#Random Numger Generator Game

#Import
import random

#Functions


print("Welcome to my guessing game!")
print("I am going to pick a number 1-10 and you will try to guess it!")
print("You will only have 4 tries only, so guess wisely!")

x = int(input("Enter a Number 0-10:"))
y = random.randint(0,10)

if x == y:
    print("Correct!")
else:
    z = input("Wrong, would you like to try again?")
if z == "yes":
    x= input("Guess Again, Enter Another Number: ")
if not z == "yes":
    print("Okay! Play again soon!")
    quit()

    
if x == y:
    print("Correct!")
else:
    z = input("Wrong, would you like to try again?")
if z == "yes":
     x= input("Guess Again, Enter Another Number: ")
if not z == "yes":
    print("Okay! Play again soon!")
    quit()
    
if x == y:
    print("Correct!")
else:
    z = input("Wrong, would you like to try again?")
if z == "yes":
     x= input("Guess Again, Enter Another Number: ")
if not z == "yes":
    print("Okay! Play again soon!")
    quit()

if x == y:
    print("Correct!")
else:
    print("You're out of guesses! The number was: " + str(y) )

    

#Main
