import csv
import numpy as np
import cv2
import os

#Load folder====================================================================

path1 = "HOG_dataset/apples"
path2 = "HOG_dataset/bananas"
files1 = []
files2 = []
for r, d, f in os.walk(path1):
    for file in f:
        if '.jpg' or '.png' in file:
            files1.append(os.path.join(r, file))

for r, d, f in os.walk(path2):
    for file in f:
        if '.jpg' or '.png' in file:
            files2.append(os.path.join(r, file))

#Create .csv file modifying the image result to 1D array========================

with open('fruit.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Fruit", "image_array"])
    for f in files1:
        image = cv2.imread(f,0)
        image = cv2.resize(image,(100,100))
        ar = np.asarray(image)
        ar = ar.flatten()
        ar_l = ar.tolist()
        writer.writerow([0,ar_l])
        print('Done')

    for f in files2:
        image = cv2.imread(f,0)
        image = cv2.resize(image,(100,100))
        ar = np.asarray(image)
        ar = ar.flatten()
        ar_l = ar.tolist()
        writer.writerow([1,ar_l])
        print('Done')
