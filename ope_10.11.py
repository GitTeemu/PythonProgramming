#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:55:46 2018

@author: olli
"""
summa = 0
while True:
    luku = int(input('Anna luku: '))
    summa += luku
    if luku == -1:
        summa += 1
        break
print('Summa: ' + str(summa))


