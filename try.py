import numpy as np
import cv2


image = cv2.imread('0.jpg',0)
ar = np.asarray(image)
print(ar.shape)
print(ar.flatten())
print(ar.tolist())
#for i in ar:
#    print(i)
