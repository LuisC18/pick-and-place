#!/usr/bin/env python

import sys                                          # System bindings
import cv2                                          # OpenCV bindings
import numpy as np

def rescaleFrame(frame, scale=.25):
  # Images, Videos and Live Video
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)

  dimensions = (width,height)

  return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

img = cv2.imread('images/reddark.jpeg')
color = rescaleFrame(img)
#color=cv2.resize(img,(700,500))
cv2.imshow('Original',color)
cv2.moveWindow("Original",0,0)
print(color.shape)


# height,width,channels = color.shape
im_gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
b,g,r = cv2.split(color)

_, mask_b = cv2.threshold(b, thresh=50, maxval=255, type=cv2.THRESH_BINARY)

_, mask_g = cv2.threshold(g, thresh=50, maxval=255, type=cv2.THRESH_BINARY)

_, mask_r = cv2.threshold(r, thresh=50, maxval=255, type=cv2.THRESH_BINARY)


cv2.imshow('mask_b',mask_b)
cv2.imshow('mask_g',mask_g)
cv2.imshow('mask_r',mask_r)


merged_mask = cv2.merge([mask_b,mask_g,mask_r])
cv2.imshow('mmerge',merged_mask)



# blank = np.zeros(color.shape[:2],dtype='uint8')
# blue = cv2.merge([b,blank,blank])
# green = cv2.merge([blank,g,blank])
# red = cv2.merge([blank,blank,r])
# cv2.imshow('Blue',blue)
# cv2.imshow('Green',green)
# cv2.imshow('Red',red)
# rgb_split = np.empty([height,width*3,3],'uint8')
# rgb_split[:, 0:width] = cv2.merge([b,b,b])
# rgb_split[:, width:width*2] = cv2.merge([g,g,g])
# rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

# cv2.imshow("Channels",rgb_split)
# cv2.moveWindow("Channels",0,height)

# hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
# h,s,v = cv2.split(hsv)
# hsv_split = np.concatenate((h,s,v),axis=1)

#cv2.imshow("Split HSV",hsv_split)
img= merged_mask.copy()


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)

imgCanny = cv2.Canny(imgBlur, 50, 150)
kernel = np.ones((3, 3))
imgDilate = cv2.dilate(imgCanny, kernel, iterations=3)
imgThre = cv2.erode(imgDilate, kernel, iterations=2)
#thresh = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
cv2.imshow("img threshold",imgThre)
#rospy.sleep(1)
_,contours, _ = cv2.findContours(imgThre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
areaList = []
approxList = []
bboxList = []
BiggestContour = []
BiggestBounding =[]
for i in contours:
  #print('Contours: ',contours)
  area = cv2.contourArea(i)
  cv2.drawContours(img, [i], -1, (255, 0, 0), 3)
  peri = cv2.arcLength(i, True)
  approx = cv2.approxPolyDP(i, 0.04 * peri, True)
  if len(approx) == 4:
    bbox = cv2.boundingRect(approx)
    areaList.append(area)
    approxList.append(approx)
    bboxList.append(bbox)

print(bboxList)



#cv2.rectangle(img,(bbox[0],bbox[1]),((bbox[0]+bbox[2]),(bbox[1]+bbox[3])),(0,255,0),3)
cv2.imshow('contour',img)
cv2.waitKey(0)
cv2.destroyAllWindows()