#!/usr/bin/env python

#Code from: https://dev.to/simarpreetsingh019/detecting-geometrical-shapes-in-an-image-using-opencv-4g72
 
import numpy as np
import cv2

img = cv2.imread('/home/khan764/ws_Robot/src/pick-and-place/RealSense_screenshot_29.06.2021.png')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
'''
In thresholding, each pixel value is compared with the threshold value. 
If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255).

Threshold is some fixed value which draws a boundary line between two set of data. Binary (Bi-valued) Image means, 
only bi or two intensity values can be used to represent the whole image. 
In image processing generally, we say a image binary when, it consists only black and white pixels.
'''
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
    elif len(approx) == 4 :
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 5 :
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10 :
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
'''
Function Info: 
approxPolyDP():
- This function calculates and approximates a polygonal curve with specified precision

approxPolyDP()
- approximates a contour shape to another shape with less number of vertices depending upon the precision we specify

drawContours(): 
- Draws the contours outlines or filled color
- To draw the contours, _cv2.drawContours function is used. 
It can also be used to draw any shape provided you have its boundary points.

BoundingRect() : 
- It gives the boundary points of the rectangle.

putText() : 
- It puts the text over the image.
'''
cv2.imshow('/home/khan764/ws_Robot/src/pick-and-place/RealSense_screenshot_29.06.2021.png')
cv2.waitkey(0)
cv2.destroyAllWindows()
























