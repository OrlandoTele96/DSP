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
cv2.imshow('imagensobremuestreada',image_up_3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Ventana Haar de 3x3.

w_haar_3=numpy.ones((1,3))
w_haar_3_3=numpy.matmul(w_haar_3.T,w_haar_3)

#interpolacion de la imagen en factor 3.

image_inter=signal.convolve2d(image_up_3,w_haar_3_3,'same').astype('uint8')
cv2.imshow('imageninterpolada',image_inter)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Filtrado de la imagen con haar.

h_soft_haar_2=numpy.ones((1,2))*(1.0/2)
h_soft_haar_2_2=numpy.matmul(h_soft_haar_2.T,h_soft_haar_2)
image_filt_haar=signal.convolve2d(image_inter,h_soft_haar_2_2,'same')
cv2.imshow('imageninterpoladaconfiltro',image_filt_haar)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Decimacion en factor 2.

image_deci_2_2=image_filt_haar[0:image_filt_haar.shape[0]:2,0:image_filt_haar.shape[1]:2]
cv2.imshow('imagendecimada',image_deci_2_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
