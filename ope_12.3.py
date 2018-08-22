#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:23:28 2018

@author: olli
"""

luvut = [5, 1, 3, 4, 2]
tahti = '*'
for i in range(len(luvut)):
    luvut[i] = luvut[i] * tahti
    
for luku in luvut:
    print(luku)
