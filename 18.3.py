#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:18:53 2018

@author: olli
"""

play = input('Play? y or yes: ')
while play == 'y' or play == 'yes':
    num = 8
    guess = int(input('Guess a number: '))
    while guess != num:
        guess = int(input('Guess again: '))
    print('Right!')
    play = input('Play? y or yes: ')
print('See you later!')
        