import cv2 
import numpy as np
import matplotlib.pyplot as plt
blood_cell = cv2.imread('bloodcell.jpg')


gray_scale_image = cv2.cvtColor(blood_cell,cv2.COLOR_BGR2GRAY)

ret,median = cv2.threshold(gray_scale_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blurred_image = cv2.GaussianBlur(median,(9,9),0)


(contours,heirachy) =cv2.findContours(blurred_image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(blurred_image,cv2.COLOR_RGBA2RGB)


if contours:
    maximum_area = 0
    largest_cell = None
    for contour in contours:
        peri = cv2.arcLength(contour,True)
        print("Perimeter:",peri)

        area = cv2.contourArea(contour)
        print("Area: ",area)

        if area > maximum_area:
            maximum_area = area
            largest_cell =contour
print("size of the largest cell = ",len(largest_cell))

cv2.drawContours(rgb,[largest_cell] , -1 ,(0,255,0),2)
cv2.imshow('rgb',rgb)
cv2.imshow('original image',gray_scale_image)
cv2.imshow('median image',median)
cv2.imshow('blurred image',blurred_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
print("number of cells :",len(contours))


 
