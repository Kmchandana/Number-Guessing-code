# number_guess_fixed.py

secret = 50     # FIXED SECRET NUMBER

print("Guess the number (between 1 and 100)!")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! You guessed the fixed secret number.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
