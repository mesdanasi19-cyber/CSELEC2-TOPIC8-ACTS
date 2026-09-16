import cv2
import numpy as np

img = cv2.imread('NoGirl.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(
    gray, cv2.HOUGH_GRADIENT,dp =1, minDist=30, param1=100, param2=30, minRadius = 10, maxRadius = 100
)
circles = np.uint16(np.around(circles))

for c in circles[0, :]:
  cv2.circle(img, (c[0], c[1]), c[2], (0, 255, 0), 2)

cv2.imshow('Detected Circles', img)
cv2.waitKey(0)