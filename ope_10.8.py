#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:03:49 2018

@author: olli
"""

ensimmainen = int(input('Ensimmäinen: '))
viimeinen = int(input('Viimeinen: '))
tulos = 0
while ensimmainen <= viimeinen:
    tulos += ensimmainen
    ensimmainen += 1
print('Summa on: ' + str(tulos))

