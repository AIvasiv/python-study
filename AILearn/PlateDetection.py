import numpy as np
import cv2
import  imutils

# Read the image.
from scipy.sparse import csr_matrix
from sklearn.preprocessing import binarize
platePicture = cv2.imread('../volvos.jpg')
e1 = cv2.getTickCount()

# Resize the image - change width to 500
platePicture = imutils.resize(platePicture, width=500)

# Display the original image
cv2.imshow("Original Image", platePicture)

# RGB to Gray scale conversion
gray = cv2.cvtColor(platePicture, cv2.COLOR_BGR2GRAY)
cv2.imshow("1 - Grayscale Conversion", gray)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("2 - Bilateral Filter", gray)

# Find Edges of the grayscale image
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("4 - Canny Edges", edged)

# Find contours based on Edges
cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('test', cnts)
cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] #sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)
NumberPlateCnt = None #we currently have no Number plate contour
e2 = cv2.getTickCount()

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))


# loop over our contours to find the best possible approximate contour of number plate
count = 0
for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4:  # Select the contour with 4 corners
            NumberPlateCnt = approx #This is our approx Number Plate Contour
            break

print('*******jaccard_similarity********');
t = (e2 - e1)/cv2.getTickFrequency()
print (t)


# Drawing the selected contour on the original image
cv2.drawContours(platePicture, [NumberPlateCnt], -1, (0,255,0), 3)
cv2.imshow("Final Image With Number Plate Detected", platePicture)

cv2.waitKey(0) #Wait for user input before closing the images displayed


