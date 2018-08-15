#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:16:05 2018

@author: olli
"""

luku = int(input('Anna luku: '))
tulos = 1
kerroin = 0
i = 0
while i < luku:
    kerroin += 1
    tulos *= kerroin
    i += 1
print('Luvun ' + str(luku) + ' kertoma on ' + str(tulos))

    
