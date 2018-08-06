#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 13:31:42 2018

@author: olli
"""

def area(shape, n):
    return shape(n)
def circle(radius):
    return 3.14*radius**2
def square(length):
    return length*length

print(area(circle, 10))
print(area(square, 5))
print(area(circle, 4/2))
