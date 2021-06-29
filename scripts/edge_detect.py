#!/usr/bin/env python

# Below code is from: https://www.thepythoncode.com/code/detect-shapes-hough-transform-opencv-python
# Edge detection -> not very good
import numpy as np
import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture(2)
# 2 is realsense camera

while True:
    _, image = cap.read()
    # convert to grayscale
    grayscale_preCrop = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscale = grayscale_preCrop[60:250, 200:500]
    cv2.imshow("Cropped grayscale",grayscale)


    # perform edge detection
    edges = cv2.Canny(grayscale, 30, 100)
    # detect lines in the image using hough lines technique
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    # iterate over the output lines and draw them
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.line(edges, (x1, y1), (x2, y2), (255, 0, 0), 3)
    # show images
    cv2.imshow("image", image)
    cv2.imshow("edges", edges)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


#	image = cv2.imread("/home/khan764/ws_Robot/src/pick-and-place/RealSense_screenshot_29.06.2021.png")




# # COde below from PyImageSearch: https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/

# # import the necessary packages
# import argparse
# import pyrealsense2 as rs
# import numpy as np
# import math
# import cv2
# import rospy
# from std_msgs.msg import *
# from os.path import join
# import imutils 

# # Configure depth and color streams
# pipeline = rs.pipeline()
# config = rs.config()

# # Get device product line for setting a supporting resolution
# pipeline_wrapper = rs.pipeline_wrapper(pipeline)
# pipeline_profile = config.resolve(pipeline_wrapper)
# device = pipeline_profile.get_device()
# device_product_line = str(device.get_info(rs.camera_info.product_line))

# config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# if device_product_line == 'L500':
#     config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
# else:
#     config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# # Starts streaming
# pipeline.start(config)

# # Wait for a coherent pair of frames: depth and color
# # frames = pipeline.wait_for_frames()
# # depth_frame = frames.get_depth_frame()
# # color_frame = frames.get_color_frame()

# # if not depth_frame or not color_frame: 
# # 	continue

# # # Converts images to numpy arrays
# # depth_image = np.asanyarray(depth_frame.get_data())
# # color_image_preCrop = np.asanyarray(color_frame.get_data())

# # #cropping the color_image to ignore table
# # color_image = color_image_preCrop[60:250, 200:500]

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the input image")
# args = vars(ap.parse_args())
# # load the image, convert it to grayscale, blur it slightly,
# # and threshold it
# image = cv2.imread(args["image"])
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# # find contours in the thresholded image
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)

# # loop over the contours
# for c in cnts:
# 	# compute the center of the contour
# 	M = cv2.moments(c)
# 	cX = int(M["m10"] / M["m00"])
# 	cY = int(M["m01"] / M["m00"])
# 	# draw the contour and center of the shape on the image
# 	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
# 	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
# 	cv2.putText(image, "center", (cX - 20, cY - 20),
# 		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
# 	# show the image
# 	cv2.imshow("Image", image)
# 	cv2.waitKey(0)











