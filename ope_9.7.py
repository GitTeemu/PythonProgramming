#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:12:04 2018

@author: olli
"""

luku1 = int(input('Anna luku: '))
luku2 = int(input('Anna toinen luku: '))
luku3 = int(input('Anna kolmas luku: '))
suuruuusjarjestys = str(sorted(luku1, luku2, luku3))
print(suuruuusjarjestys)
