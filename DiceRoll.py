# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 13:44:43 2018

@author: ewharton
"""
from random import randint



def diceroll():
    answer = "Yes"
    while answer == "Yes":
        answer = input("Would you like to roll the dice? Yes or No")
        print('You rolled a', randint(1,6))   
    if answer == "No":
            print('Bye!')
        
diceroll()