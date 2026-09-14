import cv2
img = cv2.imread('NoGirl.jpg', 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Original', img)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)