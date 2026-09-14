import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('NoGirl.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude = 20*np.log(np.abs(fshift))

plt.imshow(magnitude, cmap= 'gray')
plt.title('Magnitude Spectrum')
plt.show()