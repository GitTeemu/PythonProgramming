#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:46:41 2018

@author: olli
"""


lukuja = []
luku = 0
while luku != -1:
    luku = int(input('Anna luku: '))
    lukuja.append(luku)
lukuja.remove(-1)
suurin = max(lukuja)
pienin = min(lukuja)
print('Suurin: ' + str(suurin))
print('Pienin: ' + str(pienin))

    