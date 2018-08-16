#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:25:23 2018

@author: olli
"""

kerros = int(input('Kuinka monta kerrosta? '))
for i in range(kerros):
    for j in range(i+1):
        print('*', end='')
    print()
    