#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:43:33 2018

@author: olli
"""

pistemaara = int(input('Anna pisteet [0-60]: '))
if pistemaara <= 29:
    print('Arvosana: hylätty')
elif pistemaara <= 34:
    print('Arvosana: 1')
elif pistemaara <= 39:
    print('Arvosana: 2')
elif pistemaara <= 44:
    print('Arvosana: 3')
elif pistemaara <= 49:
    print('Arvosana: 4')
else:
    print('Arvosana: 5')
    
    