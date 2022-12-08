import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


x = np.random.randint(25,100,25)
y = np.random.randint(175,255,25)
z = np.hstack((x,y))
z = z.reshape((50,1))
z = np.float32(z)
plt.hist(z,256,[0,256])
plt.show()

X = np.random.randint(25,50,(25,2))
Y = np.random.randint(60,85,(25,2))
Z = np.vstack((X,Y))
# convert to np.float32
Z = np.float32(Z)

# Set flags (Just to avoid line break in the code)
flags = cv.KMEANS_RANDOM_CENTERS
# define criteria and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv.kmeans(Z,2,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
compactness,labels,centers = cv.kmeans(z,2,None,criteria,10,flags)
# Now separate the data, Note the flatten()
A1 = z[labels==0]
B2 = z[labels==1]
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
# Plot the data
plt.hist(A1,256,[0,256],color = 'r')
plt.hist(B2,256,[0,256],color = 'b')
plt.hist(centers,32,[0,256],color = 'y')
plt.show()

plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()