#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:36:14 2018

@author: olli
"""

luku1 = int(input('Anna ensimmäinen luku: '))
luku2 = int(input('Anna toinen luku: '))
if luku1 > luku2:
    print('Suurempi luku: ' + str(luku1))
elif luku1 < luku2:
    print('Suurempi luku: ' + str(luku2))
elif luku1 == luku2:
    print('Luvut ovat yhtä suuret!')
    
    