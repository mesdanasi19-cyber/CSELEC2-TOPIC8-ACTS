from scipy import ndimage
import numpy as np
import cv2
img = cv2.imread('NoGirl.jpg', 0)
kernel_3x3 = np.array([[-1,-1,-1], [-1,8,-1], [-1, -1, -1]])
k3 = ndimage.convolve(img, kernel_3x3)
blurred = cv2.GaussianBlur(img, (15,15), 0)
cv2.imshow('Original', img)
cv2.imshow('HPF (Edges)', k3)
cv2. imshow('LPF (Blur)', blurred)
cv2.waitKey(0)