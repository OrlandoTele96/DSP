# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:04:20 2018

@author: Jorge O. Gonzalez
"""

import numpy

def upsample(matrix,fct):
    f=numpy.copy(matrix)
    for k in range(1,fct*f.shape[0],fct):
        f=numpy.insert(f,k,numpy.zeros((fct-1,1),dtype='float32'),axis=0)
    for k in range(1,fct*f.shape[1],fct):
        f=numpy.insert(f,k,numpy.zeros((fct-1,1),dtype='float32'),axis=1)
    return f
a=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
b=upsample(a,2)
print(b)
c=upsample(a,3)
print(c)