import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Read the image
blood_cell = cv2.imread('bloodcell.jpg')

# Convert to grayscale
gray_scale_image = cv2.cvtColor(blood_cell, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding
ret, binary_image = cv2.threshold(gray_scale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(binary_image, (9, 9), 0)

# Find contours
contours, hierarchy = cv2.findContours(blurred_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Convert to RGB for drawing contours
rgb = cv2.cvtColor(blurred_image, cv2.COLOR_GRAY2RGB)

# Check if contours are found
if contours:
    # Initialize variables for biggest contour
    max_area = 0
    max_contour = None

    # Iterate through contours
    for contour in contours:
        # Calculate perimeter (arc length)
        peri = cv2.arcLength(contour, True)
        print("Perimeter:", peri)

        # Calculate area
        area = cv2.contourArea(contour)
        print("Area:", area)

        # Find the biggest contour
        if area > max_area:
            max_area = area
            max_contour = contour

    # Draw contours on the RGB image
    cv2.drawContours(rgb, [max_contour], -1, (0, 255, 0), 2)

    # Calculate the size of the biggest cell in pixels
    size_of_biggest_cell = len(max_contour)
    print("Size of the biggest cell in pixels:", size_of_biggest_cell)

    # Display the images
    cv2.imshow('RGB Image with Contours', rgb)
    cv2.imshow('Original Image', gray_scale_image)
    cv2.imshow('Binary Image', binary_image)
    cv2.imshow('Blurred Image', blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Print the total number of cells
    print("Total number of cells:", len(contours))
else:
    print("No contours found.")
