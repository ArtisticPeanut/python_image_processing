import cv2 
import numpy as np
import matplotlib.pyplot as plt
flower_img = cv2.imread('fingerprint.jpg')


gray_scale_image = cv2.cvtColor(flower_img,cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(14,7))
plt.subplot(131)
plt.title('original')
plt.imshow(gray_scale_image,cmap='gray')


threshold = 128

kernel_fliter = np.ones((7,7),np.uint8)
def morphology():
    morphology_type = cv2.MORPH_CLOSE
    perform_morphology = cv2.morphologyEx(gray_scale_image,morphology_type,kernel_fliter)

    return perform_morphology

def get_median():
    median =  cv2.medianBlur(gray_scale_image, 7)

    return median


plt.subplot(132)
plt.title('Morphology Filter')
plt.imshow(morphology(),cmap='gray')

plt.subplot(133)
plt.title('Median  Filter')
plt.imshow(get_median(),cmap='gray')

plt.show()




    




