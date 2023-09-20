import random
Easy_level_turns = 10
Hard_level_turns = 5

def set_difficulty():
    level = input("Enter what difficulty level you want 'easy' or 'hard': ")
    if level == 'easy':
        return Easy_level_turns 
    else:
        return Hard_level_turns 

def check(thinks, answer, turn):
    '''checks answer against guessed and returns remaining turns.'''
    if thinks>answer:
        print("too low")
        return turn-1
    elif thinks<answer:
        print("too high")
        return turn-1
    else:
        print(f"You got it the answer is {answer}")

def game():
    print("Welcome to the number guessing game")
    print("I am thinking of a number, can you guess it:")

    think = random.randint(1,100)



    turns = set_difficulty()
   
    guess = 0
    while guess!=think:


        print(f"You have {turns} turns left to guess the number")

        guess = int(input("Make a guess: "))
        turns = check(think, guess, turns)

        if turns == 0:
            guess = think
            print("you have run out of guesses you lose")
        elif guess!=think:
            print("Guess again")


game()