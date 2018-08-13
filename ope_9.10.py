#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:43:16 2018

@author: olli
"""

vuosi = int(input('Anna vuosi: '))
if vuosi % 4 == 0:
    print('Vuosi on karkausvuosi')
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print('Vuosi on karkausvuosi')
else:
    print('Vuosi ei ole karkausvuosi')
    

    