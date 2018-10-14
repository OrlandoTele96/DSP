# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:36:28 2018

@author: Jorge O. Gonzalez
"""

import cv2
import numpy
from scipy import signal

#Sobre sampleo.

def upsample(matrix,fct):
    f=numpy.copy(matrix)
    for k in range(1,fct*f.shape[0],fct):
        f=numpy.insert(f,k,numpy.zeros((fct-1,1),dtype='float32'),axis=0)
    for k in range(1,fct*f.shape[1],fct):
        f=numpy.insert(f,k,numpy.zeros((fct-1,1),dtype='float32'),axis=1)
    return f

#Imagen original.
imagen_original=cv2.imread('antena.png')
cv2.imshow('imagenoriginal',imagen_original)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Imagen blanco y negro

imagen_WB=cv2.imread('antena.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('imagenblanconegro',imagen_WB)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Filtrado de la imagen con filtro Haar 2x2.

h__soft_haar_2=numpy.ones((1,3))*(1/3)
h-soft_haar_2x2=numpy.matmul(h__soft_haar_2.T,h__soft_haar_2)
imagen_filt=signa.convolve2d(imagen_WB,h_soft_haar_2x2,'same').astype('uint8')

#
