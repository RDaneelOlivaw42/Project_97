from random import *

number = randrange(1, 9)

print("Number Guessing Game")
print("\nGuess a number (between 1 and 9)")

guess = int(input("Enter your guess: "))
chances = 1

while( chances < 5 ):
    if( number == guess ):
        print("You won!")
        break
    elif( number - guess >= 2 ):
        print("Your guess was too low. Try guessing a number greater than", guess)
        chances = chances + 1
        guess = int(input("Enter your guess: "))
    elif( guess - number >= 2 ):
        print("Your guess was too high. Try guessing a number less than", guess)
        chances = chances + 1
        guess = int(input("Enter your guess: "))
    elif( number - guess == 1 ):
        print("You are very close. Try guessing a number little greater than", guess)
        chances = chances + 1
        guess = int(input("Enter your guess: "))
    elif( guess - number == 1 ):
        print("You are very close. Try guessing a number little less than", guess)
        chances = chances + 1
        guess = int(input("Enter your guess: "))

if( chances >= 5 ):
    print("You lose! The number is", number)
