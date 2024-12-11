import cv2

img = cv2.imread('libro.jpg',0)
borderCanny = cv2.Canny(img,100,200)

cv2.imshow('Original', img)
cv2.imshow('blur', borderCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()
