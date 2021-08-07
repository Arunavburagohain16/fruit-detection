import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, exposure
import cv2
import os
import numpy as np

#Load dataset part to convert to HOG============================================

path = "fruit_dataset/testing/Apple" #path of the dataset images needed to convert to HOG
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' or '.png' in file:
            files.append(os.path.join(r, file))

count = 0

#HOG feature code and save======================================================

for f in files:
    image = cv2.imread(f,1)
    image = cv2.resize(image,(150,150))
    fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, multichannel=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

#Visual plot of image and HOG part==============================================

    #ax1.axis('off')
    #ax1.imshow(image, cmap=plt.cm.gray)
    #ax1.set_title('Input image')

    # Rescale histogram for better display
    #hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

    #ax2.axis('off')
    #ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
    #ax2.set_title('Histogram of Oriented Gradients')
    #plt.show()

    cv2.imwrite(str(count)+'.jpg',hog_image)
    count += 1
    if(count == 100):
        break
