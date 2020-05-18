import cv2
import numpy as np
from PIL import Image

img = cv2.imread("girl.png")
height, width, depth = np.shape(img)

# North Direction Edge
N = [[5,5,5],
     [-3,0,-3],
     [-3,-3,-3]]

# North-West Direction Edge     
NW = [[5,5,-3],
     [5,0,-3],
     [-3,-3,-3]]

# West Direction Edge     
W = [[5,-3,-3],
     [5,0,-3],
     [5,-3,-3]]

# South-West Direction Edge     
SW = [[-3,-3,-3],
     [5,0,-3],
     [5,5,-3]]      

# South Direction Edge     
S = [[-3,-3,-3],
     [-3,0,-3],
     [5,5,5]]

# South-East Direction Edge     
SE = [[-3,-3,-3],
     [-3,0,5],
     [-3,5,5]]

# East Direction Edge     
E = [[-3,-3,5],
     [-3,0,5],
     [-3,-3,5]]

# North-East Direction Edge      
NE = [[-3,5,5],
     [-3,0,5],
     [-3,-3,-3]]                                  
       
H = int(len(N))

for i in range(0, height-H):
    for j in range(0, width-H):
        summ = 0
        for k in range(0, H):
            for l in range(0, H):
                summ = summ + NE[k][l]*img[i+k][j+l]  
        if(summ[0]>255):
           summ = [255,255,255]
        elif(summ[0]<0):
           summ = [0,0,0]          
        img[i][j] = summ  
            

cv2.imshow('image',img)
cv2.waitKey(0)           
