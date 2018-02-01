# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:21:28 2018

@author: ewharton
"""

from random import randint

answer = 'Yes'
while answer == "Yes":
    answer = input("Would you like to play a game?")
    guess = int(input("Guess a number between 1 and 10"))
    actual = randint(1,10)
    if guess == actual:
        print("You win!")
    elif guess > actual:
        print("You guessed too high..")
    elif guess < actual:
        print("You guessed too low..")
if answer == "No":
    print('Bye!')    