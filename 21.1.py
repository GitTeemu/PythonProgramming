#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:45:02 2018

@author: olli
"""

def calculate_total(price, percent):
    tip = price*percent/100
    total = price + tip
    return total
    
print(calculate_total(20, 15))
print(calculate_total(28, 10))

my_price = 78.55
my_tip = 20
total = calculate_total(my_price, my_tip)
print('Total is: ', total)
