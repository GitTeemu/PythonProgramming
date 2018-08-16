#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:34:02 2018

@author: olli
"""

kierrokset = int(input('Mihin asti: '))
tulos = 0
summakerroin = 0
i = 0
while i < kierrokset:
    summakerroin += 1
    tulos += summakerroin
    i += 1
print('Summa on: ' + str(tulos))


    