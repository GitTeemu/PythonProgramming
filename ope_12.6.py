#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:40:16 2018

@author: olli
"""

luvut = [5, 1, 3, 4, 2]
print('Listan sisältö: ', end='')
print(*luvut, sep=', ')
luku1, luku2 = luvut.index(int(input('1. kohta: '))), luvut.index(int(input('2. kohta: ')))
luvut[luku1], luvut[luku2] = luvut[luku2], luvut[luku1]
print(*luvut, sep=', ')


