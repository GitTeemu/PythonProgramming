#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:35:32 2018

@author: olli
"""

tunnus = input('Anna tunnus: ')
salasana = input('Anna salasana: ')
if tunnus == 'aleksi' and salasana == 'tappara':
    print('Tappara on terästä!')
elif tunnus == 'elina' and salasana == 'kissa':
    print('Miau miau')
else:
    print('Virheellinen tunnus tai salasana!')
    
    
