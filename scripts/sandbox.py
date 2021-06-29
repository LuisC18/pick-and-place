#!/usr/bin/env python


# import pyrealsense2 as rs
# import numpy as np
# import math
# import cv2
# import rospy
# from std_msgs.msg import *
# import sensor_msgs.msg
# import geometry_msgs.msg 
# import cv2
# import imutils

# #class detectRect(object):

# # def __init__(self):
# #   super(detectRect,self).__init__()
#   # rospy.init_node('node_detectRectangle',anonymous=True)

# def callback():
#   rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

# def listener():
#   rospy.init_node('node_detectRectangle',anonymous=True)
#   rospy.Subscriber("/camera/color/image_raw", Image, callback)
#   rospy.spin()

# if __name__ == '__main__':
#   try: 
#     listener()
#   except rospy.ROSInterruptException:
#     pass

#!/usr/bin/env python
#from __future__ import print_function

#import roslib
#roslib.load_manifest('my_package')


######################################### EDGE_DETECT.PY

# #!/usr/bin/env python

# # Below code is from: https://www.thepythoncode.com/code/detect-shapes-hough-transform-opencv-python
# # Edge detection -> not very good
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2

# cap = cv2.VideoCapture(2)
# # 2 is realsense camera

# while True:
#     _, image = cap.read()
#     # convert to grayscale
#     grayscale_preCrop = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     grayscale = grayscale_preCrop[60:250, 200:500]
#     cv2.imshow("Cropped grayscale",grayscale)


#     # perform edge detection
#     edges = cv2.Canny(grayscale, 30, 100)
#     # detect lines in the image using hough lines technique
#     lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
#     # iterate over the output lines and draw them
#     for line in lines:
#         for x1, y1, x2, y2 in line:
#             cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
#             cv2.line(edges, (x1, y1), (x2, y2), (255, 0, 0), 3)
#     # show images
#     cv2.imshow("image", image)
#     cv2.imshow("edges", edges)
#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


# # image = cv2.imread("/home/khan764/ws_Robot/src/pick-and-place/RealSense_screenshot_29.06.2021.png")




##################### COde below from PyImageSearch: https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/

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
# #   continue

# # # Converts images to numpy arrays
# # depth_image = np.asanyarray(depth_frame.get_data())
# # color_image_preCrop = np.asanyarray(color_frame.get_data())

# # #cropping the color_image to ignore table
# # color_image = color_image_preCrop[60:250, 200:500]

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#   help="path to the input image")
# args = vars(ap.parse_args())
# # load the image, convert it to grayscale, blur it slightly,
# # and threshold it
# image = cv2.imread(args["image"])
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# # find contours in the thresholded image
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#   cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)

# # loop over the contours
# for c in cnts:
#   # compute the center of the contour
#   M = cv2.moments(c)
#   cX = int(M["m10"] / M["m00"])
#   cY = int(M["m01"] / M["m00"])
#   # draw the contour and center of the shape on the image
#   cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
#   cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
#   cv2.putText(image, "center", (cX - 20, cY - 20),
#     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#   # show the image
#   cv2.imshow("Image", image)
#   cv2.waitKey(0)















###################################### GEOMETRY_DETECT.PY


# #!/usr/bin/env python

# #Code from: https://dev.to/simarpreetsingh019/detecting-geometrical-shapes-in-an-image-using-opencv-4g72
 
# import numpy as np
# import cv2

# img = cv2.imread('/home/khan764/ws_Robot/src/pick-and-place/RealSense_screenshot_29.06.2021.png')
# imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
# contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# '''
# In thresholding, each pixel value is compared with the threshold value. 
# If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255).

# Threshold is some fixed value which draws a boundary line between two set of data. Binary (Bi-valued) Image means, 
# only bi or two intensity values can be used to represent the whole image. 
# In image processing generally, we say a image binary when, it consists only black and white pixels.
# '''
# for contour in contours:
#     approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
#     cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
#     x = approx.ravel()[0]
#     y = approx.ravel()[1] - 5
#     if len(approx) == 3:
#         cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
#     elif len(approx) == 4 :
#         x, y , w, h = cv2.boundingRect(approx)
#         aspectRatio = float(w)/h
#         print(aspectRatio)
#         if aspectRatio >= 0.95 and aspectRatio < 1.05:
#             cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

#         else:
#             cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

#     elif len(approx) == 5 :
#         cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     elif len(approx) == 10 :
#         cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     else:
#         cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
# '''
# Function Info: 
# approxPolyDP():
# - This function calculates and approximates a polygonal curve with specified precision

# approxPolyDP()
# - approximates a contour shape to another shape with less number of vertices depending upon the precision we specify

# drawContours(): 
# - Draws the contours outlines or filled color
# - To draw the contours, _cv2.drawContours function is used. 
# It can also be used to draw any shape provided you have its boundary points.

# BoundingRect() : 
# - It gives the boundary points of the rectangle.

# putText() : 
# - It puts the text over the image.
# '''
# cv2.imshow('/home/khan764/ws_Robot/src/pick-and-place/RealSense_screenshot_29.06.2021.png')
# cv2.waitkey(0)
# cv2.destroyAllWindows()










############################################## OBJECTRON.PY
# #!/usr/bin/env python

# # NEED PYTHON 3.0 TO RUN PROPERLY@#$@#$@#($#$(@*#$)@#$)@*#)@%^&$()

# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_objectron = mp.solutions.objectron

# # For static images:
# IMAGE_FILES = []
# with mp_objectron.Objectron(static_image_mode=True,
#                             max_num_objects=5,
#                             min_detection_confidence=0.5,
#                             model_name='Shoe') as objectron:
#   for idx, file in enumerate(IMAGE_FILES):
#     image = cv2.imread(file)
#     # Convert the BGR image to RGB and process it with MediaPipe Objectron.
#     results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#     # Draw box landmarks.
#     if not results.detected_objects:
#       #print(f'No box landmarks detected on {file}')
#       continue
#     #print(f'Box landmarks of {file}:')
#     annotated_image = image.copy()
#     for detected_object in results.detected_objects:
#       mp_drawing.draw_landmarks(
#           annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
#       mp_drawing.draw_axis(annotated_image, detected_object.rotation,
#                            detected_object.translation)
#       cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)

# # For webcam input:
# cap = cv2.VideoCapture(0)
# with mp_objectron.Objectron(static_image_mode=False,
#                             max_num_objects=5,
#                             min_detection_confidence=0.5,
#                             min_tracking_confidence=0.99,
#                             model_name='Shoe') as objectron:
#   while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
#       # If loading a video, use 'break' instead of 'continue'.
#       continue

#     # Convert the BGR image to RGB.
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     # To improve performance, optionally mark the image as not writeable to
#     # pass by reference.
#     image.flags.writeable = False
#     results = objectron.process(image)

#     # Draw the box landmarks on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.detected_objects:
#         for detected_object in results.detected_objects:
#             mp_drawing.draw_landmarks(
#               image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
#             mp_drawing.draw_axis(image, detected_object.rotation,
#                                  detected_object.translation)
#     cv2.imshow('MediaPipe Objectron', image)
#     if cv2.waitKey(5) & 0xFF == 27:
#       break
# cap.release()



####################### CONTOURS.PY
# #!/usr/bin/env python

# import numpy as np
# import cv2
# import random

# #Reading the noisy image
# #img = cv2.imread("fuzzy.png",1)

# video= cv2.VideoCapture(1)
# # external cam: 0
# # Luis webcam: 2

# check, preimg = video.read()

# img = preimg[0:200,0:200]
# #Displaying to see how it looks
# cv2.imshow("Original",img)

# #Converting the image to Gray Scale
# gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# #Removing Gaussian Noise
# blur = cv2.GaussianBlur(gray, (3,3),0)

# ####
# imgCanny = cv2.Canny(blur,0,300)
# imgDilate = cv2.dilate(imgCanny,np.ones((5,5)),iterations=3)
# imgThresh = cv2.erode(imgDilate,np.ones((5,5)),iterations=2)

# #Applying inverse binary due to white background and adapting thresholding for better results
# thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)

# #Checking to see how it looks
# #cv2.imshow("Binary",thresh)

# #Finding contours with simple retrieval (no hierarchy) and simple/compressed end points
# contours, _ = cv2.findContours(imgThresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# #Checking to see how many contours were found
# print(len(contours))

# #An empty list to store filtered contours
# filtered = []

# #Looping over all found contours
# for c in contours:
#   #If it has significant area, add to list
#   if cv2.contourArea(c) < 3000:continue
#   filtered.append(c)

# #Checking the number of filtered contours
# print(len(filtered))

# #Initialize an equally shaped image
# objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')

# #Looping over filtered contours
# for c in filtered:
#   #Select a random color to draw the contour
#   col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
#   #Draw the contour on the image with above color
#   cv2.drawContours(objects,[c], -1, col, -1)
#   #Fetch contour area
#   area = cv2.contourArea(c)
#   #Fetch the perimeter
#   p = cv2.arcLength(c,True)
#   print(area,p)

# #Finally show the processed image
# cv2.imshow("Contours",objects)
  
# # #Closing protocol
# cv2.waitKey(0)
# # cv2.destroyAllWindows()


####################################### DEPTH.PY
# #!/usr/bin/env python

# import pyrealsense2 as rs
# import numpy as np
# import math
# import cv2
# import rospy
# from std_msgs.msg import *
# import geometry_msgs.msg 
# from os.path import join



# def write():
#     print('Creating a new file')
#     path = "/home/khan764/ws_Robot/src/pick-and-place/scripts"
#     name = 'Depth_data.txt'  # Name of text file coerced with +.txt
#     return name, path

# def main():
#     try: 
#         # Configure depth and color streams
#         pipeline = rs.pipeline()
#         config = rs.config()

#         # Get device product line for setting a supporting resolution
#         pipeline_wrapper = rs.pipeline_wrapper(pipeline)
#         pipeline_profile = config.resolve(pipeline_wrapper)
#         device = pipeline_profile.get_device()
#         device_product_line = str(device.get_info(rs.camera_info.product_line))

#         config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

#         if device_product_line == 'L500':
#             config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
#         else:
#             config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

#         # Starts streaming
#         pipeline.start(config)
#         rospy.sleep(2)
#         try:
#             while True:
                

#         frames = pipeline.wait_for_frames()
#         depth_frame= frames.get_depth_frame()
#         color_frame= frames.get_color_frame()
#         #infared_frame= frames.get_infared_frame()
#         # if not depth_frame or not color_frame:
#         #     continue

#         # Converts images to numpy arrays
#         depth_image = np.asanyarray(depth_frame.get_data()) #DEPTH DATA

#         color_image = np.asanyarray(color_frame.get_data())


#         # Applys colormap on depth image (image must be converted to 8-bit per pixel first)
#         depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

#         #finds dimensions of arrays(resolution)
#         depth_colormap_dim = depth_colormap.shape
#         color_colormap_dim = color_image.shape

#         # If depth and color resolutions are different, resize color image to match depth image for display
#         if depth_colormap_dim != color_colormap_dim:
#             resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]),
#                                              interpolation=cv2.INTER_AREA)
#             images = np.hstack((resized_color_image, depth_colormap))
#         else:
#             images = np.hstack((color_image, depth_colormap))

#         # Show images
#         cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
#         img_color = depth_colormap.copy()
#         cv2.imshow(img_color)

#         print(depth_colormap)
#         name, path = write()
#         file = open(join(path, name),'w')   # Trying to create a new file or open one
#         file.write(depth_colormap)
#         file.close()
#         print('wrote to file')

#     except rospy.ROSInterruptException:
#       exit()
#     except KeyboardInterrupt:
#       exit()


# if __name__ == '__main__':
#   main()

############################### DEPTH_TUTORIAL

# #!/usr/bin/env python

# # First import the library
# import pyrealsense2 as rs
# import rospy

# try:
#     # Create a context object. This object owns the handles to all connected realsense devices
#     pipeline = rs.pipeline()

#     # Configure streams
#     config = rs.config()
#     config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

#     # Start streaming
#     pipeline.start(config)

#     while True:
#         # This call waits until a new coherent set of frames is available on a device
#         # Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
#         frames = pipeline.wait_for_frames()
#         depth = frames.get_depth_frame()
#         if not depth: continue

#         dist = depth.get_distance(250,250)
#         dist1 = depth.get_distance(400,400)
#         print ('250',dist)
#         print('400',dist1)
#         rospy.sleep(5)
#         #Print a simple text-based representation of the image, by breaking it into 10x20 pixel regions and approximating the coverage of pixels within one meter
#         coverage = [0]*64
#         for y in range(480):
#             for x in range(640):
#                 dist = depth.get_distance(x, y)
#                 print(dist)
#                 if 0 < dist and dist < 1:
#                     coverage[x//10] += 1
            
#             if y%20 is 19:
#                 line = ""
#                 for c in coverage:
#                     line += " .:nhBXWW"[c//25]
#                 coverage = [0]*64
#                 #print(line)

#     exit(0)
# #except rs.error as e:
# #    # Method calls agaisnt librealsense objects may throw exceptions of type pylibrs.error
# #    print("pylibrs.error was thrown when calling %s(%s):\n", % (e.get_failed_function(), e.get_failed_args()))
# #    print("    %s\n", e.what())
# #    exit(1)
# except Exception as e:
#     print(e)
#     pass