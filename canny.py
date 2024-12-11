#Bibliotecas
import cv2
#captura información de la webcam
#Abrir imagen
img = cv2.imread('libro.jpg',0)
#Aplicar canny
borderCanny = cv2.Canny(img,100,200)
#Mostrar imagenes
cv2.imshow('Original', img)
cv2.imshow('blur', borderCanny)
#presionar una tecla para ejecutar
cv2.waitKey(0)
cv2.destroyAllWindows()
