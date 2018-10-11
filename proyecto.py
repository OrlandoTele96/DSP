import numpy
import cv2
import numpy
from scipy import signal

"""
cv2.imread() carga una imagen .jpg que este contenida en la carpeta donde
estemos ejecutando el programa.
cv2.imshow() muestra la imagen seleccionada.

cv2.waitkey() espera un tiempo indeterminado para cerrar la imagen.
"""
imagen = cv2.imread('Molly.jpg')
cv2.imshow('imagen',imagen)
cv2.waitKey(0)


"""
cv2.destroyAllWindows() nos permite cerrar las ventanas de imagenes generadas
"""
cv2.destroyAllWindows()


"""
Recordemos que cv2.imread('imagen.jpg') es un comando que es capaz de cargar una imagen
.jpg a nuestro programa, ahora, si agregamos el parametro
('imagen.jpg', cv2.IMREAD_GRAYSCALE) cargaremos nuestra imagen, pero la
transformara en solo una escala de grises.
"""
imagen2 = cv2.imread('Molly.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('imagen2',imagen2)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""
la función img.shape nos ayuda a obtener las medidas de nuestra imagen, pero
si nosotros usamos la función cv2.resize() no tendremos que obtener las
medias previamente. Por eso lo comentamos.
"""
#height, width = img.shape[:2]

"""
La función cv2.resize() nos permite modificar el tamaño de una imagen, usando dos coordenadas, en este caso
fx y fy, las cuales, segun el problema, podremos modificarlas a partir del tamaño original multiplicando
por un número (mayor a 1 para amplificar, y menor a 1 para reducir)
"""
imagen2 = cv2.resize(imagen2, (0,0), fx=1.5, fy=1.5)

cv2.imshow("MollyAmplificada", imagen2)

cv2.waitKey(0)
cv2.destroyAllWindows()
