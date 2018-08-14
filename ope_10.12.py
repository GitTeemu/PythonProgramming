#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:13:41 2018

@author: olli
"""

summa = 0
lukuja = 0
while True:
    luku = int(input('Anna luku: '))
    summa += luku
    lukuja += 1
    if luku == -1:
        summa += 1
        lukuja -= 1
        break
print('Summa: ' + str(summa))
print('Lukuja: ' + str(lukuja))
