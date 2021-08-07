import cv2
import matplotlib.pyplot as plt

import cv2
import os
import numpy as np


#HOG feature code and save
image = cv2.imread(f,1)
image = cv2.resize(image,(150,150))
fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                cells_per_block=(1, 1), visualize=True, multichannel=True)
