import csv
import numpy as np
import cv2
import os

#Create test dataset fruit_test.csv=============================================

path1 = "HOG_dataset/banana_test"
files1 = []

for r, d, f in os.walk(path1):
    for file in f:
        if '.jpg' or '.png' in file:
            files1.append(os.path.join(r, file))

choice = input("Enter the test fruit name of dataset : ")
with open('fruit_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Fruit", "image_array"])
    for f in files1:
        image = cv2.imread(f,0)
        image = cv2.resize(image,(100,100))
        ar = np.asarray(image)
        ar = ar.flatten()
        ar_l = ar.tolist()
        if(choice.lower() == "apple"):
            writer.writerow([0,ar_l])
        elif(choice.lower() == "banana"):
            writer.writerow([1,ar_l])

        print('Done')
