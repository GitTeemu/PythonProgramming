#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:45:34 2018

@author: olli
"""

ensimmainen = int(input('Anna luku: '))
viimeinen = int(input('Anna toinen luku: '))
if ensimmainen < viimeinen:
    while ensimmainen <= viimeinen:
        print(ensimmainen)
        ensimmainen = ensimmainen + 1
elif ensimmainen > viimeinen:
    while ensimmainen >= viimeinen:
        print(ensimmainen)
        ensimmainen = ensimmainen - 1
        
        