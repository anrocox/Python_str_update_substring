#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

In a string python how to change the value of a substring?

En un string python ¿como modificar el valor de un substring?
'''

#create a str
s = 'red truck, yellow truck, red truck, yellow truck'
print(s)

#the strings are immutable, so you can not update substrings
#can use the replace() method if needs to update a substring regardless of the
#amount of times that repeat in the string.
s_new = s.replace('truck', 'lorry')
print(s_new)

#using merge of strings with the + operator to add an substring,
#create new string.
s_new = s[:11] + 'green' + s[17:]
print(s_new)
