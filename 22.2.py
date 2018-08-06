#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:11:29 2018

@author: olli
"""
def person(age):
    print("I am a person")
    def student(major):
        print("I like learning")
        def vacation(place):
            print("But I need to take breaks")
            print(age,"|",major,"|",place)
        return vacation
    return student

person(29)("CS")("Japan")
person(23)("Law")("Florida")