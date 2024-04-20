import cv2 
import numpy as np
import matplotlib.pyplot as plt
flower_img = cv2.imread('number2.jpg')

cv2.imshow('Input image',flower_img)

gray_scale_image = cv2.cvtColor(flower_img,cv2.COLOR_BGR2GRAY)

cv2.imshow('gray',gray_scale_image)
threshold = 128
##performing manual threshhodling as tuple
(thresholding,flower_binary) = cv2.threshold(gray_scale_image,threshold,255,cv2.THRESH_BINARY)
binary_flower_shape = flower_binary.shape # S

#manual threshholding
kernel_fliter = np.ones((7,7),np.uint8)


filter_shape = kernel_fliter.shape #f
##converting from 255 range to 0 to 1

flower_binary = flower_binary/255

#defining the rows and columns
columns = binary_flower_shape[1] + filter_shape[1] -1 
rows = binary_flower_shape[0] + filter_shape[0] -1 

print(rows)

#padding the imag es 
Padded_image = np.copy(flower_binary)
Padded_image = np.pad(Padded_image, ((3,3),(3,3)), mode ='constant', constant_values=0)

result = np.zeros_like(flower_binary)

for i in range (rows - filter_shape[0]+ 1):
    for j in range(columns - filter_shape[1] + 1):
       

        window_range = Padded_image[i:i + filter_shape[0], j:j + filter_shape[1]]
        result[i,j] = np.any(window_range == kernel_fliter)
       
#removing the small objects by opening 
goal =np.uint8
adjust_image = np.ones((16,16),goal)
final_result  = cv2.morphologyEx(result.astype(goal),cv2.MORPH_OPEN,adjust_image)
cv2.imshow('output image ',final_result*255) 
cv2.waitKey(0)
