#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:43:34 2018

@author: olli
"""

counter = 0
for num in range(2, 100, 2):
    if num % 6 == 0:
        counter += 1
print(counter, 'numbers are even and divisible by 6')
        