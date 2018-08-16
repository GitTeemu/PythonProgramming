#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:54:38 2018

@author: olli
"""

import random

arvattava = random.randint(0, 1000)
arvaus = 0
while arvaus != arvattava:
    arvaus = int(input('Arvaa luku: '))
    if arvaus < arvattava:
        print('Liian pieni!')
    elif arvaus > arvattava:
        print('Liian suuri!')
print('Oikein!')

