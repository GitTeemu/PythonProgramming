#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:52:47 2018

@author: olli
"""

valinta = int(input('Valitse luku (ei lukua 10 tai 100): '))
valitsiOikein = False
if valinta != 10 and valinta != 100:
    valitsiOikein = True
    
if valitsiOikein:
    print('Hyvin valittu')
else:
    print('Soo soo')
    
    