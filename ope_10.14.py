#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:24:16 2018

@author: olli
"""

summa = 0
lukuja = 0
parillisia = 0
parittomia = 0
luku = 0
while luku != -1:
    luku = int(input('Anna luku: '))
    summa += luku
    lukuja += 1
    if luku % 2 == 0:
        parillisia += 1
    elif luku % 2 != 0:
        parittomia += 1
summa += 1
lukuja -= 1
parittomia -= 1
ka = summa / lukuja
print('Summa: ' + str(summa))
print('Lukuja: ' + str(lukuja))
print('Keskiarvo: ' + str(ka))
print('Parillisia: ' + str(parillisia))
print('Parittomia: ' + str(parittomia))
