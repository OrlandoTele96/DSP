# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:36:28 2018

@author: Jorge O. Gonzalez
"""
#Bibliotecas.

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
image_original=cv2.imread('antena.png')
cv2.imshow('imagenoriginal',image_original)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Imagen blanco y negro

image_WB=cv2.imread('antena.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('imagenblanconegro',image_WB)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Sobre muestreo de la imagen.

image_up_3=upsample(image_WB,3)

#Ventana Haar de 3x3.

w_haar_3=numpy.ones((1,3))
w_haar_3_3=numpy.matmul(w_haar_3.T,w_haar_3)

#interpolacion de la imagen en factor 3.

image_inter=signal.convolve2d(image_up_3,w_haar_3_3,'same').astype('uint8')

#Decimacion en factor 2.
