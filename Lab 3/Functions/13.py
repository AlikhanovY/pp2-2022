import random
name=input("Hello! What is your name?")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
ran_number=random.randint(1,20)
guess=int
times=0
while guess != ran_number:
    print("Take a guess")
    guess=int(input())
    times=times+1
    if guess < ran_number:
        print("Your guess is too low.")
    elif guess > ran_number:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {times} guesses!")