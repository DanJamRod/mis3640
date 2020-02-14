import random

def guess():
    """ Runs a game where player has to guess a random integer between 1 and 20 in 6 guesses
    """
    print(f"Hello! What is your name?")
    name = input()
    number = random.randint(1,20)
    print(f"{name}, I am thinking of a number betwen 1 and 20.")
    count = 0
    while count < 6:
        print (f"Take a guess")
        a = input()
        a = int(a)
        count = count + 1
        if a > number:
            print(f"Your guess is too high")
        elif a < number:
            print (f"Your guess is too low")
        else:
            print (f"Well done! You guessed my number in {count} guesses")
            break
    if a != number:
        print(f"I'm sorry, but you didn't manage to guess my number in 6 guesses :( My number was {number}")
    
    print(f"Would you like to play again?(y/n)")
    play = input()
    if play in "yesYesYES":
       guess()
    else:
        print(f"Goodbye!")

guess()