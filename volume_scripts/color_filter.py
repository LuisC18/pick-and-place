#!/usr/bin/env python

import sys                                          # System bindings
import cv2                                          # OpenCV bindings
import numpy as np

class colorFilter:
  def __init__(self,frame):
    if isinstance(frame,str) == True:
      #local image
      image = cv2.imread(frame)
      self.original = self.rescaleFrame(image)

    else:
      #live image
      self.original = self.rescaleFrame(frame)

    cv2.imshow('Original',self.original)
    cv2.moveWindow("Original",0,0)

  def rescaleFrame(self,frame, scale=1.5):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

  def filterBackground(self):
    #split image to rgb channels
    b,g,r = cv2.split(self.original)

    #binary threshold any color values above "60", greater than 60 -> 255, less than 60 -> 0 
    _, mask_b = cv2.threshold(b, thresh=60, maxval=255, type=cv2.THRESH_BINARY_INV)

    _, mask_g = cv2.threshold(g, thresh=60, maxval=255, type=cv2.THRESH_BINARY_INV)

    _, mask_r = cv2.threshold(r, thresh=60, maxval=255, type=cv2.THRESH_BINARY_INV)


    # cv2.imshow('mask_b',mask_b)
    # cv2.imshow('mask_g',mask_g)
    # cv2.imshow('mask_r',mask_r)

    #merge the thresholded rgb channels together to create a mask of cube
    merged_mask = cv2.merge([mask_b,mask_g,mask_r])
    #cv2.imshow('merged_mask',merged_mask)

    #grayscale merged_mask
    gray_merge = cv2.cvtColor(merged_mask, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray_merge',gray_merge)

    #bw merged mask
    _, mask_merge_bw = cv2.threshold(gray_merge, thresh=200, maxval=255, type=cv2.THRESH_BINARY)
    #cv2.imshow('merged_mask_bw',mask_merge_bw)

    
    #cv2.rectangle(original,(bbox[0],bbox[1]),((bbox[0]+bbox[2]),(bbox[1]+bbox[3])),(0,255,255),3)
    return gray_merge