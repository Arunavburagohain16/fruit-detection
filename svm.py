import numpy as np
import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, exposure
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd
import json
import cv2

#Load Dataset part==============================================================

dataset = pd.read_csv('fruit.csv')
dataset_test = pd.read_csv('fruit_test.csv')
calorie_read = pd.read_csv('fruit_calorie.csv')

X = dataset.iloc[:,1].values
y = dataset.iloc[:,0].values
X_t = []
for i in X:
    a = json.loads(i)
    X_t.append(a)

#SVM Part=======================================================================

from sklearn import svm

clf = svm.SVC(kernel='linear')
clf.fit(X_t, y)

print(clf.score(X_t, y))

#Graph plot part================================================================
#Not working
'''
plt.plot(X_t, y)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

'''

X_t1 = []
X_test = dataset_test.iloc[:,1].values
for i in X_test:
    a = json.loads(i)
    X_t1.append(a)

y1 = dataset_test.iloc[:,0].values

#print("Value of X : ",clf.predict(X_t1))
predic_result = clf.predict(X_t1)
print(clf.score(X_t1, y1))


#Calorie detection part ========================================================

fru = calorie_read.iloc[:,0].values
calo = calorie_read.iloc[:,1].values

for i in predic_result:
    fruit = fru[i]
    calorie = calo[i]
    print("Detected Fruit : ",fruit," Calorie : ",calorie)




#Calorie detect using Dictionary================================================
'''
fruit_calorie = {'Apple':59,'Banana':89,'Grape':72}

for i in predic_result:
    fru = list(fruit_calorie.keys())[i]
    fru_calorie = fruit_calorie[fru]
    print("Detected : ",fru," Calorie : ",fru_calorie)


'''

#print("Value of y : ",y)

#Test for single image==========================================================
#Not working
'''

img = cv2.imread('7.jpg')
img =cv2.resize(img,(100,100))
fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1), visualize=True, multichannel=True)
#cv2.imwrite('Hog.jpg',hog_image)

#hog_image = cv2.imread('Hog.jpg',0)
num_img = np.asarray(hog_image)
ar = num_img.flatten()
ar = ar.tolist()
ar = [ar]
#print(len(X_t1[0]))
#ar = ar.reshape(1, -1)
#print(ar)
print("Value of X : ",clf.predict(ar))
'''
