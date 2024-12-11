#Bibliotecas
import cv2

capture = cv2.VideoCapture(0)
while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        #Aplicar canny
        borderCanny = cv2.Canny(frame,100,200)
        #Mostrar imagenes
        cv2.imshow('Original', frame)
        cv2.imshow('blur', borderCanny)
        #presionar una tecla para ejecutar
        if (cv2.waitKey(1) == ord('s')):
                break
    else:
        break
capture.release()
cv2.destroyAllWindows()
