#1ST CODE
#youtuber = "ksi"

#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

#2ND CODE
#adj = input("Adjective: ")
#verb1 = input("Verb: ")
#verb2 = input("Verb: ")
#famous_person = input("Famous person: ")

#madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
#i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

#print(madlib)

#3RD CODE 
#import random 

#def guess(x):
#    random_number = random.randint(1, x)
#    guess = 0
#    while guess != random_number:
#        guess = int(input(f'Guess a number between 1 and {x}:'))
#        if guess < random_number:
#            print('Sorry,guess again. Too low.')
#        elif guess > random_number:
#            print('Sorry, guess again. Too high')

#    print(f'Yay, congrats. You have guessed the number {random_number} correctly')

#def computuer_guess(x):
#    low = 1
#    high = x
#    feedback = ''
#    while feedback != 'c':
#        if low != high:
#            guess = random.randint(low, high)
#        else:
#            guess = low
#        feedback = input(f'is {guess} to high (H), too low (L), or correct (C)??').lower()
#        if feedback == 'h':
#            high = guess - 1
#        elif feedback == 'l':
#            low = guess + 1
#    print(f'Yay! The computer guessed your number, {guess}, correctly!')

#guess(10)


#4TH CODE 
#import random 

#def guess(X):
#    random_number = random.randint(1, X)  
#    guess = 0
#    while guess != random_number:
#        guess = int(input(f'Guess a number between 1 and {X}: '))
#        if guess < random_number:
#            print('Sorry, guess again. Too low.')
#        elif guess > random_number:
#            print('Sorry, guess again. Too high.')
#    print(f'Yay, congrats. You have guessed the number {random_number} correctly!')  
#guess(100

#5th CODE
#import random

#def play():
#    user = input("Whats your choice? 'r' for rock, 'p'for paper, 's' for scissors\n")
#    computer = random.choice(['r', 'p', 's'])

#    if user == computer:
#        return 'Its\'s a tie'

#    if is_win(user, computer):
#        return 'You own!'
    
#    return 'You lost'

#def is_win(player, opponent):
#    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
#        or (player == 'p' and opponent == 'r'):
#        return True

#print(play)

import math
import random

class Player:
    def_int_(self, letter):
        self.letter = letter 
    
    def get_move(self, lettter):
        super()._init_(letter)
    
    def get_mover(self, game):
        pass

class RandomComputerPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)
        
    def _init_(self,game):
        pass

class